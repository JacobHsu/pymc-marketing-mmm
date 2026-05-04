"""Unit tests for components/mmm_runner.py.

Scope: pure functions and branches testable without MCMC sampling.
Skipped: build_mmm, fit_mmm, sample_posterior_predictive, load_mmm
         (require real PyMC model or fitted .nc file).
"""
from __future__ import annotations

import os
from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd
import pytest

import components.mmm_runner as mmm_runner
from components.mmm_runner import (
    ensure_model_file,
    get_channel_roas,
    load_sample_data,
    prepare_features,
    save_mmm,
    saved_model_exists,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_raw_df(n: int = 10) -> pd.DataFrame:
    """Minimal raw DataFrame matching the mock_cgp CSV schema."""
    rng = np.random.default_rng(0)
    return pd.DataFrame(
        {
            "Weeks": pd.date_range("2020-01-06", periods=n, freq="W"),
            "target1": rng.uniform(100, 500, n),
            "Google Search": rng.uniform(1, 10, n),
            "DV360": rng.uniform(1, 10, n),
            "Facebook": rng.uniform(1, 10, n),
            "AMS": rng.uniform(1, 10, n),
            "TV": rng.uniform(1, 10, n),
            "VOD": rng.uniform(1, 10, n),
            "OOH": rng.uniform(1, 10, n),
            "Radio": rng.uniform(1, 10, n),
            "Numeric Distribution": rng.uniform(0, 1, n),
            "RSP": rng.uniform(0, 1, n),
            "Promotion": rng.uniform(0, 1, n),
        }
    )


# ---------------------------------------------------------------------------
# prepare_features
# ---------------------------------------------------------------------------

class TestPrepareFeatures:
    def test_y_not_in_X(self):
        data = pd.DataFrame({"y": [1, 2], "a": [3, 4], "b": [5, 6]})
        X, y = prepare_features(data)
        assert "y" not in X.columns

    def test_y_values_match(self):
        data = pd.DataFrame({"y": [10, 20, 30], "a": [1, 2, 3]})
        _, y = prepare_features(data)
        assert list(y) == [10, 20, 30]

    def test_X_preserves_all_non_y_columns(self):
        data = pd.DataFrame({"y": [1], "ch1": [2], "ctrl": [3], "t": [0]})
        X, _ = prepare_features(data)
        assert set(X.columns) == {"ch1", "ctrl", "t"}

    def test_returns_series_for_y(self):
        data = pd.DataFrame({"y": [1.0, 2.0], "x": [0.0, 0.0]})
        _, y = prepare_features(data)
        assert isinstance(y, pd.Series)

    def test_single_row(self):
        data = pd.DataFrame({"y": [5], "feat": [99]})
        X, y = prepare_features(data)
        assert len(X) == 1
        assert len(y) == 1


# ---------------------------------------------------------------------------
# saved_model_exists
# ---------------------------------------------------------------------------

class TestSavedModelExists:
    def test_true_when_file_exists(self, tmp_path):
        f = tmp_path / "model.nc"
        f.write_text("dummy")
        assert saved_model_exists(str(f)) is True

    def test_false_when_no_file_and_no_hf(self, tmp_path):
        with patch.object(mmm_runner, "HF_REPO_ID", ""):
            assert saved_model_exists(str(tmp_path / "nope.nc")) is False

    def test_true_when_no_file_but_hf_repo_set(self, tmp_path):
        with patch.object(mmm_runner, "HF_REPO_ID", "owner/repo"):
            assert saved_model_exists(str(tmp_path / "nope.nc")) is True


# ---------------------------------------------------------------------------
# ensure_model_file
# ---------------------------------------------------------------------------

class TestEnsureModelFile:
    def test_no_op_when_file_exists(self, tmp_path):
        f = tmp_path / "model.nc"
        f.write_text("dummy")
        # Should return without raising
        ensure_model_file(str(f))

    def test_raises_when_no_file_and_no_hf(self, tmp_path):
        with patch.object(mmm_runner, "HF_REPO_ID", ""):
            with pytest.raises(FileNotFoundError, match="HF_REPO_ID"):
                ensure_model_file(str(tmp_path / "missing.nc"))

    def test_error_message_contains_path(self, tmp_path):
        target = str(tmp_path / "missing.nc")
        with patch.object(mmm_runner, "HF_REPO_ID", ""):
            with pytest.raises(FileNotFoundError, match="missing.nc"):
                ensure_model_file(target)

    def test_downloads_from_hf_when_repo_set_same_path(self, tmp_path):
        target = str(tmp_path / "model.nc")
        with patch.object(mmm_runner, "HF_REPO_ID", "owner/repo"):
            with patch("huggingface_hub.hf_hub_download", return_value=target) as mock_dl:
                ensure_model_file(target)
                mock_dl.assert_called_once()

    def test_downloads_from_hf_copies_when_path_differs(self, tmp_path):
        target = str(tmp_path / "model.nc")
        cached = str(tmp_path / "cached" / "model.nc")
        os.makedirs(str(tmp_path / "cached"), exist_ok=True)
        (tmp_path / "cached" / "model.nc").write_text("cached content")
        with patch.object(mmm_runner, "HF_REPO_ID", "owner/repo"):
            with patch("huggingface_hub.hf_hub_download", return_value=cached):
                ensure_model_file(target)
                assert os.path.exists(target)


# ---------------------------------------------------------------------------
# load_sample_data
# ---------------------------------------------------------------------------

class TestLoadSampleData:
    @patch("components.mmm_runner.pd.read_csv")
    def test_returns_dataframe_and_meta(self, mock_csv):
        mock_csv.return_value = _make_raw_df()
        df, meta = load_sample_data()
        assert isinstance(df, pd.DataFrame)
        assert isinstance(meta, dict)

    @patch("components.mmm_runner.pd.read_csv")
    def test_date_column_renamed(self, mock_csv):
        mock_csv.return_value = _make_raw_df()
        df, _ = load_sample_data()
        assert "date_week" in df.columns
        assert "Weeks" not in df.columns

    @patch("components.mmm_runner.pd.read_csv")
    def test_target_column_renamed_to_y(self, mock_csv):
        mock_csv.return_value = _make_raw_df()
        df, _ = load_sample_data()
        assert "y" in df.columns
        assert "target1" not in df.columns

    @patch("components.mmm_runner.pd.read_csv")
    def test_time_index_added(self, mock_csv):
        mock_csv.return_value = _make_raw_df(n=5)
        df, _ = load_sample_data()
        assert "t" in df.columns
        assert list(df["t"]) == [0, 1, 2, 3, 4]

    @patch("components.mmm_runner.pd.read_csv")
    def test_zero_channels_dropped(self, mock_csv):
        raw = _make_raw_df()
        raw["Google Search"] = 0.0
        mock_csv.return_value = raw
        _, meta = load_sample_data()
        assert "Google Search" not in meta["channel_cols"]
        assert "Google Search" in meta["_dropped_channels"]

    @patch("components.mmm_runner.pd.read_csv")
    def test_nonzero_channels_kept(self, mock_csv):
        mock_csv.return_value = _make_raw_df()
        _, meta = load_sample_data()
        # All channels have nonzero spend in _make_raw_df
        assert "Google Search" in meta["channel_cols"]

    @patch("components.mmm_runner.pd.read_csv")
    def test_meta_has_dropped_channels_key(self, mock_csv):
        mock_csv.return_value = _make_raw_df()
        _, meta = load_sample_data()
        assert "_dropped_channels" in meta

    @patch("components.mmm_runner.pd.read_csv")
    def test_unknown_dataset_raises(self, mock_csv):
        with pytest.raises(KeyError):
            load_sample_data("nonexistent_dataset")


# ---------------------------------------------------------------------------
# get_channel_roas
# ---------------------------------------------------------------------------

def _make_mmm_mock(channels: list[str], contributions: list[float]) -> MagicMock:
    """Build a minimal MMM mock with predictable idata.posterior."""
    mmm = MagicMock()
    mmm.channel_columns = channels

    def sel_side_effect(channel):
        idx = channels.index(channel)
        inner = MagicMock()
        inner.mean.return_value.sum.return_value = contributions[idx]
        return inner

    mmm.idata.posterior.__getitem__.return_value.sel.side_effect = sel_side_effect
    return mmm


class TestGetChannelROAS:
    def test_returns_dataframe(self):
        mmm = _make_mmm_mock(["ch1"], [100.0])
        data = pd.DataFrame({"ch1": [10.0, 20.0]})
        result = get_channel_roas(mmm, data)
        assert isinstance(result, pd.DataFrame)

    def test_one_row_per_channel(self):
        mmm = _make_mmm_mock(["ch1", "ch2"], [100.0, 50.0])
        data = pd.DataFrame({"ch1": [10.0], "ch2": [5.0]})
        result = get_channel_roas(mmm, data)
        assert len(result) == 2

    def test_roas_calculation(self):
        mmm = _make_mmm_mock(["ch1"], [90.0])
        data = pd.DataFrame({"ch1": [30.0, 15.0]})  # total spend = 45
        result = get_channel_roas(mmm, data)
        assert result["ROAS"].iloc[0] == pytest.approx(90.0 / 45.0)

    def test_zero_spend_roas_is_zero(self):
        mmm = _make_mmm_mock(["ch1"], [100.0])
        data = pd.DataFrame({"ch1": [0.0, 0.0]})
        result = get_channel_roas(mmm, data)
        assert result["ROAS"].iloc[0] == 0.0

    def test_required_columns_present(self):
        mmm = _make_mmm_mock(["ch1"], [100.0])
        data = pd.DataFrame({"ch1": [10.0]})
        result = get_channel_roas(mmm, data)
        assert set(result.columns) == {"頻道", "總貢獻（銷售額）", "總花費", "ROAS"}

    def test_channel_names_in_result(self):
        mmm = _make_mmm_mock(["Google Search", "TV"], [80.0, 40.0])
        data = pd.DataFrame({"Google Search": [10.0], "TV": [5.0]})
        result = get_channel_roas(mmm, data)
        assert set(result["頻道"]) == {"Google Search", "TV"}


# ---------------------------------------------------------------------------
# save_mmm
# ---------------------------------------------------------------------------

class TestSaveMmm:
    def test_returns_path(self, tmp_path):
        mmm = MagicMock()
        path = str(tmp_path / "model.nc")
        result = save_mmm(mmm, path)
        assert result == path

    def test_calls_mmm_save(self, tmp_path):
        mmm = MagicMock()
        path = str(tmp_path / "model.nc")
        save_mmm(mmm, path)
        mmm.save.assert_called_once_with(path)

    def test_creates_parent_directory(self, tmp_path):
        mmm = MagicMock()
        nested = str(tmp_path / "new_dir" / "model.nc")
        save_mmm(mmm, nested)
        assert os.path.isdir(str(tmp_path / "new_dir"))


# ---------------------------------------------------------------------------
# load_mmm
# ---------------------------------------------------------------------------

class TestLoadMmm:
    def test_calls_ensure_and_load(self, tmp_path):
        path = str(tmp_path / "model.nc")
        fake_mmm = MagicMock()
        with patch.object(mmm_runner, "ensure_model_file") as mock_ensure:
            with patch.object(mmm_runner.MMM, "load", return_value=fake_mmm) as mock_load:
                from components.mmm_runner import load_mmm
                result = load_mmm(path)
                mock_ensure.assert_called_once_with(path)
                mock_load.assert_called_once_with(path)
                assert result is fake_mmm
