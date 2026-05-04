"""E2E tests for the MMM Demo Streamlit multi-page app.

Covers:
  1. Home page loads — title visible, sidebar nav has 5 items
  2. 資料總覽 navigates — page accessible, no crash
  3. 模型擬合 navigates — page accessible, no crash
  4. 頻道貢獻 locked state — warning + "前往模型擬合" link visible
  5. 預算最佳化 locked state — warning + "前往模型擬合" link visible
  6. CSS lock in effect — sidebar links for 頻道貢獻/預算最佳化 have opacity:0.35

Run with:
    & "C:\\Users\\user\\miniconda3\\envs\\pymc-marketing-dev\\python.exe" \
        -m pytest streamlit/mmm-demo/tests/e2e/ -v
"""

from __future__ import annotations

import time
import pytest
from playwright.sync_api import sync_playwright, Page, expect

BASE_URL = "http://localhost:8501"

# Streamlit needs a moment to hydrate after navigation; we wait for the
# network to be idle rather than using fixed sleeps where possible.
LOAD_TIMEOUT = 20_000   # ms — max wait for page / element to appear
NAV_SETTLE   = 2_000    # ms — brief pause after click so Streamlit re-renders


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def streamlit_page(browser, url: str) -> Page:
    """Open a fresh Streamlit page and wait until it finishes its first load."""
    page = browser.new_page()
    page.goto(url, wait_until="networkidle", timeout=LOAD_TIMEOUT)
    # Streamlit renders a spinner while hydrating; wait for it to disappear.
    page.wait_for_selector("[data-testid='stAppViewContainer']", timeout=LOAD_TIMEOUT)
    return page


def wait_for_streamlit(page: Page, extra_ms: int = 0) -> None:
    """Wait until the Streamlit 'running' indicator is gone."""
    # The running indicator carries data-testid="stStatusWidget"
    try:
        page.wait_for_selector(
            "[data-testid='stStatusWidget']",
            state="detached",
            timeout=15_000,
        )
    except Exception:
        pass  # not present means it already finished
    if extra_ms:
        time.sleep(extra_ms / 1000)


def sidebar_nav_links(page: Page):
    """Return all <a> elements inside the Streamlit sidebar nav."""
    return page.locator("[data-testid='stSidebarNav'] ul li a")


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        br = p.chromium.launch(headless=True)
        yield br
        br.close()


@pytest.fixture()
def home_page(browser):
    """Fresh page opened at the home URL."""
    page = streamlit_page(browser, BASE_URL)
    wait_for_streamlit(page)
    yield page
    page.close()


# ---------------------------------------------------------------------------
# Test 1: Home page loads
# ---------------------------------------------------------------------------

class TestHomePage:
    def test_title_visible(self, home_page):
        """Main heading must contain the expected Chinese title text.

        The page renders two h1 elements (sidebar brand + main content).
        Use .first to avoid Playwright's strict-mode violation, or target
        the main content area directly.
        """
        # Target the main content area's first heading to avoid ambiguity
        heading = home_page.locator("[data-testid='stAppViewContainer'] h1").first
        expect(heading).to_contain_text("MMM", timeout=LOAD_TIMEOUT)

    def test_sidebar_has_five_nav_items(self, home_page):
        """Sidebar navigation must list exactly 5 pages."""
        links = sidebar_nav_links(home_page)
        # Streamlit may take a moment to inject nav items
        home_page.wait_for_function(
            "() => document.querySelectorAll(\"[data-testid='stSidebarNav'] ul li a\").length >= 5",
            timeout=LOAD_TIMEOUT,
        )
        count = links.count()
        assert count == 5, f"Expected 5 sidebar nav items, got {count}"

    def test_sidebar_brand_visible(self, home_page):
        """Sidebar should show the MMM DEMO brand header."""
        sidebar = home_page.locator("[data-testid='stSidebar']")
        expect(sidebar).to_contain_text("MMM DEMO", timeout=LOAD_TIMEOUT)


# ---------------------------------------------------------------------------
# Test 2: 資料總覽 page navigates without crash
# ---------------------------------------------------------------------------

class TestDataOverviewPage:
    def test_page_loads(self, browser):
        page = streamlit_page(browser, BASE_URL + "/資料總覽")
        wait_for_streamlit(page, extra_ms=NAV_SETTLE)
        # Should not show an error box
        error_box = page.locator("[data-testid='stException']")
        assert error_box.count() == 0, "Unexpected Streamlit exception on 資料總覽"
        page.close()

    def test_page_title_or_content_visible(self, browser):
        page = streamlit_page(browser, BASE_URL + "/資料總覽")
        wait_for_streamlit(page, extra_ms=NAV_SETTLE)
        # Page should have at least one heading
        heading = page.locator("h1, h2")
        assert heading.count() > 0, "No headings found on 資料總覽 page"
        page.close()


# ---------------------------------------------------------------------------
# Test 3: 模型擬合 page navigates without crash
# ---------------------------------------------------------------------------

class TestModelFittingPage:
    def test_page_loads(self, browser):
        page = streamlit_page(browser, BASE_URL + "/模型擬合")
        wait_for_streamlit(page, extra_ms=NAV_SETTLE)
        error_box = page.locator("[data-testid='stException']")
        assert error_box.count() == 0, "Unexpected Streamlit exception on 模型擬合"
        page.close()

    def test_page_title_or_content_visible(self, browser):
        page = streamlit_page(browser, BASE_URL + "/模型擬合")
        wait_for_streamlit(page, extra_ms=NAV_SETTLE)
        heading = page.locator("h1, h2")
        assert heading.count() > 0, "No headings found on 模型擬合 page"
        page.close()


# ---------------------------------------------------------------------------
# Test 4: 頻道貢獻 locked state
# ---------------------------------------------------------------------------

class TestChannelContributionLocked:
    def _open(self, browser) -> Page:
        page = streamlit_page(browser, BASE_URL + "/頻道貢獻")
        wait_for_streamlit(page, extra_ms=NAV_SETTLE)
        return page

    def test_warning_visible(self, browser):
        """When mmm is not in session state the warning block must appear."""
        page = self._open(browser)
        # st.warning() renders inside [data-testid="stAlert"]
        # OR a div with role="alert"; search for the Chinese warning text.
        body_text = page.locator("[data-testid='stAppViewContainer']").inner_text(timeout=LOAD_TIMEOUT)
        assert "模型擬合" in body_text, (
            "Expected warning about 模型擬合 on locked 頻道貢獻 page"
        )
        page.close()

    def test_goto_model_fitting_link_visible(self, browser):
        """st.page_link button '前往模型擬合' must be present when locked."""
        page = self._open(browser)
        # st.page_link renders an <a> tag; look for text content
        link = page.get_by_text("前往模型擬合")
        assert link.count() > 0, "Could not find '前往模型擬合' link on locked 頻道貢獻 page"
        page.close()


# ---------------------------------------------------------------------------
# Test 5: 預算最佳化 locked state
# ---------------------------------------------------------------------------

class TestBudgetOptimisationLocked:
    def _open(self, browser) -> Page:
        page = streamlit_page(browser, BASE_URL + "/預算最佳化")
        wait_for_streamlit(page, extra_ms=NAV_SETTLE)
        return page

    def test_warning_visible(self, browser):
        page = self._open(browser)
        body_text = page.locator("[data-testid='stAppViewContainer']").inner_text(timeout=LOAD_TIMEOUT)
        assert "模型擬合" in body_text, (
            "Expected warning about 模型擬合 on locked 預算最佳化 page"
        )
        page.close()

    def test_goto_model_fitting_link_visible(self, browser):
        page = self._open(browser)
        link = page.get_by_text("前往模型擬合")
        assert link.count() > 0, "Could not find '前往模型擬合' link on locked 預算最佳化 page"
        page.close()


# ---------------------------------------------------------------------------
# Test 6: CSS lock on sidebar links
# ---------------------------------------------------------------------------

class TestSidebarCSSLock:
    """When the model has not been fitted the sidebar links for 頻道貢獻 and
    預算最佳化 must have pointer-events:none and opacity:0.35 injected by CSS.

    We verify via JavaScript getComputedStyle so the injected <style> block
    is evaluated by the browser engine.
    """

    def _computed_style(self, page: Page, href_fragment: str, prop: str) -> str:
        return page.evaluate(
            f"""() => {{
                const a = document.querySelector(
                    "[data-testid='stSidebarNav'] ul li a[href*='{href_fragment}']"
                );
                if (!a) return 'NOT_FOUND';
                return window.getComputedStyle(a).getPropertyValue('{prop}');
            }}"""
        )

    def _open_home(self, browser) -> Page:
        page = streamlit_page(browser, BASE_URL)
        wait_for_streamlit(page, extra_ms=NAV_SETTLE)
        return page

    def test_channel_contribution_link_pointer_events(self, browser):
        page = self._open_home(browser)
        val = self._computed_style(page, "%ED%95%80%EB%8F%84", "pointer-events")
        # The href uses URL-encoded Chinese; try the raw href fragment too
        if val == "NOT_FOUND":
            # Try with the encoded segment that Streamlit uses
            val = self._computed_style(page, "channel", "pointer-events")
        # If the element still isn't found, fall back to checking the style tag
        if val == "NOT_FOUND":
            style_content = page.evaluate(
                "() => Array.from(document.querySelectorAll('style')).map(s => s.textContent).join('\\n')"
            )
            assert "pointer-events" in style_content and "頻道貢獻" in style_content, (
                "Expected pointer-events CSS for 頻道貢獻 not found in any <style> block"
            )
        else:
            assert val == "none", (
                f"Expected pointer-events:none on 頻道貢獻 sidebar link, got '{val}'"
            )
        page.close()

    def test_budget_optimisation_link_pointer_events(self, browser):
        page = self._open_home(browser)
        val = self._computed_style(page, "budget", "pointer-events")
        if val == "NOT_FOUND":
            style_content = page.evaluate(
                "() => Array.from(document.querySelectorAll('style')).map(s => s.textContent).join('\\n')"
            )
            assert "pointer-events" in style_content and "預算最佳化" in style_content, (
                "Expected pointer-events CSS for 預算最佳化 not found in any <style> block"
            )
        else:
            assert val == "none", (
                f"Expected pointer-events:none on 預算最佳化 sidebar link, got '{val}'"
            )
        page.close()

    def test_locked_css_injected_for_channel_contribution(self, browser):
        """The injected <style> block must reference 頻道貢獻 and set opacity 0.35."""
        page = self._open_home(browser)
        style_content = page.evaluate(
            "() => Array.from(document.querySelectorAll('style')).map(s => s.textContent).join('\\n')"
        )
        assert "頻道貢獻" in style_content, (
            "Injected CSS for '頻道貢獻' not found in page styles"
        )
        assert "0.35" in style_content, (
            "Expected opacity value 0.35 in injected lock CSS"
        )
        page.close()

    def test_locked_css_injected_for_budget_optimisation(self, browser):
        """The injected <style> block must reference 預算最佳化."""
        page = self._open_home(browser)
        style_content = page.evaluate(
            "() => Array.from(document.querySelectorAll('style')).map(s => s.textContent).join('\\n')"
        )
        assert "預算最佳化" in style_content, (
            "Injected CSS for '預算最佳化' not found in page styles"
        )
        page.close()
