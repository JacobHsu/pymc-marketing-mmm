---
theme: seriph
title: AI 開發流實戰
mdc: true
transition: fade-out
layout: cover
background: '#ffffff'
---

<div class="flex flex-col justify-center h-full px-16">
  <div class="w-14 h-14 mb-8 bg-gradient-to-br from-indigo-500 to-sky-400 rounded-2xl flex items-center justify-center">
    <span class="text-white text-2xl font-bold">AI</span>
  </div>
  <h1 class="text-6xl font-bold text-slate-900 leading-tight mb-4">
    AI 開發流實戰
  </h1>
  <p class="text-2xl text-slate-500 mb-10">
    從 mmm-demo 到 Claude Code 工作法
  </p>
  <p class="text-base text-slate-400">Jacob Hsu &nbsp;·&nbsp; 2026.05</p>
</div>

---

## 分享地圖

<div class="grid grid-cols-3 gap-6 mt-10">
  <div class="border border-indigo-100 rounded-2xl p-6 shadow-sm bg-white">
    <div class="text-3xl mb-3">🔬</div>
    <div class="text-lg font-bold text-slate-800 mb-2">What</div>
    <div class="text-slate-500">mmm-demo 做了什麼</div>
  </div>
  <div class="border border-indigo-100 rounded-2xl p-6 shadow-sm bg-white">
    <div class="text-3xl mb-3">⚡</div>
    <div class="text-lg font-bold text-slate-800 mb-2">How</div>
    <div class="text-slate-500">AI 開發流怎麼跑</div>
  </div>
  <div class="border border-indigo-100 rounded-2xl p-6 shadow-sm bg-white">
    <div class="text-3xl mb-3">💡</div>
    <div class="text-lg font-bold text-slate-800 mb-2">Lessons</div>
    <div class="text-slate-500">踩過的坑</div>
  </div>
</div>

---

## PyMC-Marketing 是什麼

<div class="grid grid-cols-2 gap-10 mt-6 items-start">
  <div>
    <div class="text-slate-500 text-sm mb-5">PyMC Labs 出品的開源貝葉斯行銷分析庫</div>
    <div class="space-y-4">
      <div class="flex items-start gap-3">
        <span class="bg-indigo-100 text-indigo-700 font-bold text-xs px-2 py-1 rounded shrink-0">MMM</span>
        <span class="text-slate-600 text-sm">Media Mix Modeling — 量化各渠道廣告效益</span>
      </div>
      <div class="flex items-start gap-3">
        <span class="bg-sky-100 text-sky-700 font-bold text-xs px-2 py-1 rounded shrink-0">CLV</span>
        <span class="text-slate-600 text-sm">Customer Lifetime Value — 預測顧客終身價值</span>
      </div>
      <div class="flex items-start gap-3">
        <span class="bg-green-100 text-green-700 font-bold text-xs px-2 py-1 rounded shrink-0">CSA</span>
        <span class="text-slate-600 text-sm">Customer Segmentation & Attribution</span>
      </div>
    </div>
    <div class="mt-6 flex gap-2 flex-wrap">
      <span class="bg-slate-100 text-slate-500 text-xs px-3 py-1 rounded-full">Apache 2.0</span>
      <span class="bg-slate-100 text-slate-500 text-xs px-3 py-1 rounded-full">完整不確定性量化</span>
      <span class="bg-slate-100 text-slate-500 text-xs px-3 py-1 rounded-full">PyMC Labs 維護</span>
    </div>
  </div>
  <div class="bg-indigo-50 border border-indigo-100 rounded-2xl p-5">
    <div class="text-indigo-500 font-bold text-sm mb-4">為什麼選 PyMC-Marketing？</div>
    <div class="space-y-3 text-xs text-slate-600">
      <div class="flex items-start gap-2"><span class="text-green-500 font-bold shrink-0">✓</span> 完整不確定性量化 — 給信心區間，不只是數字</div>
      <div class="flex items-start gap-2"><span class="text-green-500 font-bold shrink-0">✓</span> 開源透明，模型假設可審計、可修改</div>
      <div class="flex items-start gap-2"><span class="text-green-500 font-bold shrink-0">✓</span> Apache 2.0，商業使用無限制</div>
      <div class="flex items-start gap-2"><span class="text-green-500 font-bold shrink-0">✓</span> PyMC Labs 持續維護，社群活躍</div>
    </div>
  </div>
</div>

---

## 什麼是 Media Mix Modeling？

<div class="mt-4">
  <div class="text-xl text-slate-600 mb-6 text-center">
    你知道花了多少錢在廣告，<br/>但你不知道
    <span class="text-red-400 font-bold">哪個渠道真的有效</span>
  </div>
  <div class="grid grid-cols-3 gap-4">
    <div class="bg-indigo-50 border border-indigo-100 rounded-xl p-4 text-center">
      <div class="text-2xl mb-2">⏱️</div>
      <div class="font-bold text-indigo-700 text-sm mb-1">Adstock</div>
      <div class="text-slate-500 text-xs">廣告遞延效果<br/>今天曝光，下週才見效</div>
    </div>
    <div class="bg-sky-50 border border-sky-100 rounded-xl p-4 text-center">
      <div class="text-2xl mb-2">📈</div>
      <div class="font-bold text-sky-700 text-sm mb-1">飽和曲線</div>
      <div class="text-slate-500 text-xs">報酬遞減定律<br/>多投不等於多賺</div>
    </div>
    <div class="bg-green-50 border border-green-100 rounded-xl p-4 text-center">
      <div class="text-2xl mb-2">🎯</div>
      <div class="font-bold text-green-700 text-sm mb-1">貝葉斯推斷</div>
      <div class="text-slate-500 text-xs">量化不確定性<br/>給信心區間，不是點估計</div>
    </div>
  </div>
  <div class="mt-5 bg-slate-50 rounded-xl p-3 font-mono text-xs text-center text-slate-500">
    廣告支出 → <span class="text-indigo-500 font-semibold">Adstock 轉換</span> → <span class="text-sky-500 font-semibold">飽和曲線</span> → <span class="text-green-600 font-semibold">各渠道銷售貢獻</span>
  </div>
</div>

---

## mmm-demo 是什麼

<div class="grid grid-cols-2 gap-10 mt-6 items-start">
  <div>
    <div class="mb-6">
      <div class="text-sm font-semibold text-indigo-500 uppercase tracking-wider mb-1">Pain Point</div>
      <div class="text-xl text-slate-700">行銷預算分配靠直覺，<br/>渠道 ROI 說不清楚</div>
    </div>
    <div class="mb-6">
      <div class="text-sm font-semibold text-indigo-500 uppercase tracking-wider mb-1">Solution</div>
      <div class="text-xl text-slate-700">Media Mix Model 量化<br/>各渠道對銷售的貢獻</div>
    </div>
    <div>
      <div class="text-sm font-semibold text-indigo-500 uppercase tracking-wider mb-1">Stack</div>
      <div class="flex gap-2 mt-1 flex-wrap">
        <span class="bg-indigo-50 text-indigo-700 text-sm px-3 py-1 rounded-full">PyMC-Marketing</span>
        <span class="bg-sky-50 text-sky-700 text-sm px-3 py-1 rounded-full">Streamlit</span>
        <span class="bg-slate-100 text-slate-600 text-sm px-3 py-1 rounded-full">Python</span>
      </div>
    </div>
  </div>
  <div class="space-y-2">
    <div class="bg-sky-50 border border-sky-200 rounded-xl p-4">
      <div class="text-sky-600 font-bold text-sm mb-1">UI 層 — Streamlit</div>
      <div class="text-slate-500 text-xs">參數輸入 / 圖表渲染 / Streamlit Cloud 部署</div>
    </div>
    <div class="text-center text-slate-300 text-lg">↕</div>
    <div class="bg-indigo-50 border border-indigo-200 rounded-xl p-4">
      <div class="text-indigo-600 font-bold text-sm mb-1">模型層 — PyMC-Marketing</div>
      <div class="text-slate-500 text-xs">MMM 建模 / MCMC 採樣 / 貢獻度分解</div>
    </div>
    <div class="text-center text-slate-300 text-lg">↕</div>
    <div class="bg-slate-50 border border-slate-200 rounded-xl p-4">
      <div class="text-slate-600 font-bold text-sm mb-1">資料層 — CSV / ArviZ</div>
      <div class="text-slate-500 text-xs">合成廣告資料 / InferenceData 序列化</div>
    </div>
  </div>
</div>

---
layout: center
---

<div class="text-center">
  <h2 class="text-4xl font-bold text-slate-800 mb-3">Live Demo</h2>
  <a href="https://pymc-marketing-mmm.streamlit.app" target="_blank" class="text-lg text-indigo-400 hover:text-indigo-600 no-underline hover:underline hover:underline-offset-4 transition-colors">https://pymc-marketing-mmm.streamlit.app</a>
  <div class="grid grid-cols-3 gap-5 mt-8 text-left max-w-2xl mx-auto">
    <div class="bg-slate-50 rounded-xl p-4">
      <div class="text-indigo-500 font-bold text-sm mb-1">① 選渠道</div>
      <div class="text-slate-500 text-xs">勾選要分析的廣告渠道（TV / Social / Search）</div>
    </div>
    <div class="bg-slate-50 rounded-xl p-4">
      <div class="text-indigo-500 font-bold text-sm mb-1">② 跑模型</div>
      <div class="text-slate-500 text-xs">點 Run Model，MCMC 採樣約 30 秒完成</div>
    </div>
    <div class="bg-slate-50 rounded-xl p-4">
      <div class="text-indigo-500 font-bold text-sm mb-1">③ 看貢獻</div>
      <div class="text-slate-500 text-xs">Channel Contribution 圖表顯示各渠道 ROI</div>
    </div>
  </div>
</div>

---

## AI 開發流全貌

<div class="mt-6 flex flex-col items-center gap-0">
  <div class="bg-indigo-50 border border-indigo-200 rounded-xl px-8 py-3 text-indigo-800 font-semibold">User Intent</div>
  <div class="text-slate-300 text-2xl">↓</div>
  <div class="bg-indigo-500 text-white rounded-xl px-8 py-3 font-semibold">Claude Code — Plan Mode</div>
  <div class="flex gap-4 items-start mt-1">
    <div class="flex flex-col items-center">
      <div class="text-slate-300 text-2xl">↓</div>
      <div class="bg-slate-100 border border-slate-200 rounded-xl px-6 py-2 text-slate-700 text-sm">CLAUDE.md<br/><span class="text-slate-400">行為規則</span></div>
    </div>
    <div class="flex flex-col items-center">
      <div class="text-slate-300 text-2xl">↓</div>
      <div class="bg-slate-100 border border-slate-200 rounded-xl px-6 py-2 text-slate-700 text-sm">Memory / Tasks<br/><span class="text-slate-400">跨對話記憶</span></div>
    </div>
  </div>
  <div class="text-slate-300 text-2xl">↓</div>
  <div class="bg-sky-500 text-white rounded-xl px-8 py-3 font-semibold">Agents / Skills</div>
  <div class="text-slate-300 text-2xl">↓</div>
  <div class="flex gap-3">
    <div class="bg-green-50 border border-green-200 text-green-700 rounded-lg px-4 py-2 text-sm">Code</div>
    <div class="bg-green-50 border border-green-200 text-green-700 rounded-lg px-4 py-2 text-sm">Tests</div>
    <div class="bg-green-50 border border-green-200 text-green-700 rounded-lg px-4 py-2 text-sm">Docs</div>
  </div>
</div>

<div class="absolute bottom-12 right-12 text-slate-400 text-sm italic">AI 不是替代，是「第二大腦 + 執行引擎」</div>

---

## Claude Code 怎麼用

<div class="grid grid-cols-2 gap-8 mt-6">
  <div class="border border-slate-100 rounded-2xl p-6">
    <div class="text-indigo-500 font-bold text-lg mb-3">① Plan Mode</div>
    <div class="text-slate-600 mb-4">先想再做 — 防止 AI 衝動行事</div>
    <div class="bg-slate-900 rounded-xl p-4 text-sm font-mono">
      <div class="text-slate-400"># 任何複雜任務都能觸發</div>
      <div class="text-green-400">/plan</div>
      <div class="text-slate-500 mt-2">→ Claude 只讀不動</div>
      <div class="text-slate-500">→ 你確認計畫後才執行</div>
    </div>
  </div>
  <div class="border border-slate-100 rounded-2xl p-6">
    <div class="text-indigo-500 font-bold text-lg mb-3">② CLAUDE.md + Memory</div>
    <div class="text-slate-600 mb-4">讓 AI 記住你的偏好與限制</div>
    <div class="bg-slate-900 rounded-xl p-4 text-sm font-mono">
      <div class="text-slate-400"># CLAUDE.md 裡的規則</div>
      <div class="text-yellow-400 mt-1">只做被要求的事</div>
      <div class="text-yellow-400">不改沒必要改的地方</div>
      <div class="text-slate-500 mt-2">→ AI 不會自作主張</div>
    </div>
  </div>
</div>

---

## Agents / Skills 架構

<div class="mt-6">
  <div class="text-slate-500 mb-4">每個 agent 只做一件事，context 不污染</div>
  <table class="w-full text-sm">
    <thead>
      <tr class="border-b border-slate-100">
        <th class="text-left py-2 pr-6 text-indigo-500 font-semibold">Agent</th>
        <th class="text-left py-2 text-slate-500 font-normal">任務</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-slate-50">
      <tr>
        <td class="py-3 pr-6 font-mono text-slate-800">planner</td>
        <td class="py-3 text-slate-600">拆解任務、產生實作計畫</td>
      </tr>
      <tr>
        <td class="py-3 pr-6 font-mono text-slate-800">tdd-guide</td>
        <td class="py-3 text-slate-600">先寫測試，再補實作（RED → GREEN → REFACTOR）</td>
      </tr>
      <tr>
        <td class="py-3 pr-6 font-mono text-slate-800">code-reviewer</td>
        <td class="py-3 text-slate-600">每次改完自動審查，抓 correctness / security</td>
      </tr>
      <tr>
        <td class="py-3 pr-6 font-mono text-slate-800">security-reviewer</td>
        <td class="py-3 text-slate-600">commit 前掃描，確認沒有硬編碼金鑰或敏感資訊</td>
      </tr>
    </tbody>
  </table>
</div>

---

## 踩坑 — Context 管理

<div class="grid grid-cols-2 gap-8 mt-6">
  <div class="border-l-4 border-red-300 pl-4">
    <div class="font-bold text-red-500 mb-3">❌ 坑 1：Context 耗盡，AI 開始幻覺</div>
    <div class="text-slate-600 text-sm mb-3">
      對話太長後，API 名稱突然錯誤、邏輯開始繞圈，<br/>
      AI 在「自信」地胡說。
    </div>
    <div class="bg-slate-50 rounded-lg p-3 text-sm text-slate-500">
      解法：定期 <span class="font-mono text-indigo-600">/compact</span>，<br/>
      重要資訊存 memory，不要堆在對話裡
    </div>
  </div>
  <div class="border-l-4 border-red-300 pl-4">
    <div class="font-bold text-red-500 mb-3">❌ 坑 2：一次給太多指令</div>
    <div class="text-slate-600 text-sm mb-3">
      「幫我做 A、B、C、D」— AI 做完 A 就開始<br/>
      自行詮釋 B，最後跑偏到你不認識的地方。
    </div>
    <div class="bg-slate-50 rounded-lg p-3 text-sm text-slate-500">
      解法：一次一個 Todo，<br/>
      完成確認後再下一個指令
    </div>
  </div>
</div>

---

## 踩坑 — AI 過度設計

<div class="grid grid-cols-2 gap-8 mt-6">
  <div class="border-l-4 border-orange-300 pl-4">
    <div class="font-bold text-orange-500 mb-3">❌ 坑 3：AI 幫你加你沒要求的功能</div>
    <div class="text-slate-600 text-sm mb-3">
      改一個 button，AI「順手」幫你加了<br/>
      abstract base class、config flag、error handling。
    </div>
    <div class="bg-slate-50 rounded-lg p-3 text-sm text-slate-500">
      解法：CLAUDE.md 明文寫<br/>
      <span class="font-mono text-orange-600">No features beyond what was asked</span>
    </div>
  </div>
  <div class="border-l-4 border-orange-300 pl-4">
    <div class="font-bold text-orange-500 mb-3">❌ 坑 4：AI 改了不該改的地方</div>
    <div class="text-slate-600 text-sm mb-3">
      修一個 bug，AI 順手 refactor 了周圍代碼，<br/>
      diff 突然多了 300 行。
    </div>
    <div class="bg-slate-50 rounded-lg p-3 text-sm text-slate-500">
      解法：Surgical Changes 原則<br/>
      + code-reviewer agent 把關每次 diff
    </div>
  </div>
</div>

---
layout: section
---

# Claude Code Plugin 生態評鑑
以 mmm-demo 為測試場，系統性驗證 3 個 Plugin 套件、13 Skills、9 Agents

---

## Plugin 套件介紹

<div class="grid grid-cols-3 gap-5 mt-5 text-xs">
  <div class="border border-indigo-100 rounded-2xl p-4">
    <div class="text-indigo-500 font-bold text-sm mb-3">superpowers</div>
    <div class="space-y-2.5">
      <div>
        <span class="font-mono text-slate-800">refactor-clean</span>
        <span class="text-slate-400 ml-2">死碼清理師</span>
      </div>
      <div>
        <span class="font-mono text-slate-800">python-review</span>
        <span class="text-slate-400 ml-2">Python 審查員</span>
      </div>
      <div>
        <span class="font-mono text-slate-800">tdd-workflow</span>
        <span class="text-slate-400 ml-2">測試驅動教練</span>
      </div>
      <div>
        <span class="font-mono text-slate-800">security-review</span>
        <span class="text-slate-400 ml-2">安全審查員</span>
      </div>
    </div>
  </div>
  <div class="border border-sky-100 rounded-2xl p-4">
    <div class="text-sky-500 font-bold text-sm mb-3">gstack</div>
    <div class="space-y-2.5">
      <div>
        <span class="font-mono text-slate-800">design-review</span>
        <span class="text-slate-400 ml-2">會寫程式的設計師</span>
      </div>
      <div>
        <span class="font-mono text-slate-800">design-shotgun</span>
        <span class="text-slate-400 ml-2">設計探索者</span>
      </div>
      <div>
        <span class="font-mono text-slate-800">benchmark</span>
        <span class="text-slate-400 ml-2">效能工程師</span>
      </div>
      <div>
        <span class="font-mono text-slate-800">cso</span>
        <span class="text-slate-400 ml-2">資安長</span>
      </div>
      <div>
        <span class="font-mono text-slate-800">canary</span>
        <span class="text-slate-400 ml-2">系統可靠性工程師(SRE)</span>
      </div>
    </div>
  </div>
  <div class="border border-green-100 rounded-2xl p-4">
    <div class="text-green-500 font-bold text-sm mb-3">agency-agents</div>
    <div class="space-y-2.5">
      <div>
        <span class="font-mono text-slate-800">e2e-runner</span>
        <span class="text-slate-400 ml-2">E2E 自動化工程師</span>
      </div>
      <div>
        <span class="font-mono text-slate-800">Explore</span>
        <span class="text-slate-400 ml-2">程式碼探索員（內建）</span>
      </div>
    </div>
  </div>
</div>
---

## 完整品質流水線

<div class="absolute inset-x-10 top-24 bottom-4 flex flex-col gap-1">

  <!-- Row 1: 代碼品質 → -->
  <div class="text-xs font-bold text-indigo-400 mb-1">▸ 代碼品質</div>
  <div class="flex items-center gap-1">
    <div class="flex-1 bg-indigo-50 border border-indigo-200 rounded-xl py-2.5 px-2 text-center">
      <div class="font-bold text-indigo-700 text-sm">重構</div>
      <div class="font-mono text-indigo-400 text-xs mt-0.5">refactor-clean</div>
      <div class="text-slate-400 text-xs mt-0.5">移除死碼</div>
    </div>
    <div class="text-indigo-300 text-2xl font-bold shrink-0">→</div>
    <div class="flex-1 bg-indigo-50 border border-indigo-200 rounded-xl py-2.5 px-2 text-center">
      <div class="font-bold text-indigo-700 text-sm">安全掃描</div>
      <div class="font-mono text-indigo-400 text-xs mt-0.5">security-review</div>
      <div class="text-slate-400 text-xs mt-0.5">PR diff 把關</div>
    </div>
    <div class="text-indigo-300 text-2xl font-bold shrink-0">→</div>
    <div class="flex-1 bg-indigo-50 border border-indigo-200 rounded-xl py-2.5 px-2 text-center">
      <div class="font-bold text-indigo-700 text-sm">單元測試</div>
      <div class="font-mono text-indigo-400 text-xs mt-0.5">python-review</div>
      <div class="text-slate-400 text-xs mt-0.5">邏輯正確性</div>
    </div>
  </div>

  <!-- 右側向下箭頭：mirror row structure，對齊最右節點中心 -->
  <div class="flex items-center gap-1">
    <div class="flex-1"></div>
    <div class="text-2xl font-bold shrink-0 invisible">→</div>
    <div class="flex-1"></div>
    <div class="text-2xl font-bold shrink-0 invisible">→</div>
    <div class="flex-1 text-center"><span class="text-3xl font-black text-slate-300">↓</span></div>
  </div>

  <!-- Row 2: 產品品質 ← 反向 -->
  <div class="text-xs font-bold text-sky-400 mb-1">▸ 產品品質</div>
  <div class="flex items-center gap-1">
    <div class="flex-1 bg-sky-50 border border-sky-200 rounded-xl py-2.5 px-2 text-center">
      <div class="font-bold text-sky-700 text-sm">E2E 自動化</div>
      <div class="font-mono text-sky-400 text-xs mt-0.5">e2e-runner</div>
      <div class="text-slate-400 text-xs mt-0.5">流程自動測試</div>
    </div>
    <div class="text-sky-300 text-2xl font-bold shrink-0">←</div>
    <div class="flex-1 bg-sky-50 border border-sky-200 rounded-xl py-2.5 px-2 text-center">
      <div class="font-bold text-sky-700 text-sm">QA</div>
      <div class="font-mono text-sky-400 text-xs mt-0.5">qa</div>
      <div class="text-slate-400 text-xs mt-0.5">真實瀏覽器驗證</div>
    </div>
    <div class="text-sky-300 text-2xl font-bold shrink-0">←</div>
    <div class="flex-1 bg-sky-50 border border-sky-200 rounded-xl py-2.5 px-2 text-center">
      <div class="font-bold text-sky-700 text-sm">UI 審查</div>
      <div class="font-mono text-sky-400 text-xs mt-0.5">design-review</div>
      <div class="text-slate-400 text-xs mt-0.5">截圖驅動 UX</div>
    </div>
  </div>

  <!-- 左側向下箭頭：mirror row structure，對齊最左節點中心 -->
  <div class="flex items-center gap-1">
    <div class="flex-1 text-center"><span class="text-3xl font-black text-slate-300">↓</span></div>
    <div class="text-2xl font-bold shrink-0 invisible">←</div>
    <div class="flex-1"></div>
    <div class="text-2xl font-bold shrink-0 invisible">←</div>
    <div class="flex-1"></div>
  </div>

  <!-- Row 3: 上線維運 → -->
  <div class="text-xs font-bold text-green-400 mb-1">▸ 上線維運</div>
  <div class="flex items-center gap-1">
    <div class="flex-1 bg-green-50 border border-green-200 rounded-xl py-2.5 px-2 text-center">
      <div class="font-bold text-green-700 text-sm">部署</div>
      <div class="font-mono text-green-400 text-xs mt-0.5">setup-deploy</div>
      <div class="text-slate-400 text-xs mt-0.5">環境腳本化</div>
    </div>
    <div class="text-green-300 text-2xl font-bold shrink-0">→</div>
    <div class="flex-1 bg-green-50 border border-green-200 rounded-xl py-2.5 px-2 text-center">
      <div class="font-bold text-green-700 text-sm">效能基線</div>
      <div class="font-mono text-green-400 text-xs mt-0.5">benchmark</div>
      <div class="text-slate-400 text-xs mt-0.5">建立比較數字</div>
    </div>
    <div class="text-green-300 text-2xl font-bold shrink-0">→</div>
    <div class="flex-1 bg-green-50 border border-green-200 rounded-xl py-2.5 px-2 text-center">
      <div class="font-bold text-green-700 text-sm">Canary 監控</div>
      <div class="font-mono text-green-400 text-xs mt-0.5">canary</div>
      <div class="text-slate-400 text-xs mt-0.5">持續健康偵測</div>
    </div>
  </div>

</div>

---

## Plugin Skills 實際帶來了什麼

<div class="grid grid-cols-3 gap-3 mt-3">

  <div class="border border-indigo-100 rounded-2xl p-3">
    <div class="text-indigo-500 font-bold text-sm mb-1">🎨 design-review</div>
    <div class="text-slate-500 text-xs mb-2">截圖驅動 UI 審查</div>
    <div class="flex items-center gap-2 mb-1">
      <span class="bg-slate-100 text-slate-400 text-xs px-2 py-0.5 rounded shrink-0">沒用前</span>
      <span class="text-slate-500 text-xs">UI 改完，肉眼看沒問題</span>
    </div>
    <div class="flex items-center gap-2 mb-2">
      <span class="bg-indigo-100 text-indigo-600 text-xs px-2 py-0.5 rounded shrink-0">用了後</span>
      <span class="text-slate-700 text-xs font-semibold">鎖定頁沒有「返回」連結<br/>使用者會直接卡住</span>
    </div>
    <div class="text-slate-400 text-xs italic">截圖才看得到的 UX 死角</div>
  </div>

  <div class="border border-sky-100 rounded-2xl p-3">
    <div class="text-sky-500 font-bold text-sm mb-1">🤖 e2e-runner</div>
    <div class="text-slate-500 text-xs mb-2">全自主 E2E 自動化</div>
    <div class="flex items-center gap-2 mb-1">
      <span class="bg-slate-100 text-slate-400 text-xs px-2 py-0.5 rounded shrink-0">沒用前</span>
      <span class="text-slate-500 text-xs">0 個 E2E 測試<br/>（Playwright 太麻煩，跳過）</span>
    </div>
    <div class="flex items-center gap-2 mb-2">
      <span class="bg-sky-100 text-sky-600 text-xs px-2 py-0.5 rounded shrink-0">用了後</span>
      <span class="text-slate-700 text-xs font-semibold">15 個測試全 PASS<br/>完全不用自己寫 Playwright</span>
    </div>
    <div class="text-slate-400 text-xs italic">Agent 自主產出 → 執行 → 修復 → 回報</div>
  </div>

  <div class="border border-green-100 rounded-2xl p-3">
    <div class="text-green-500 font-bold text-sm mb-1">🎯 design-shotgun</div>
    <div class="text-slate-500 text-xs mb-2">系統性 UI 風格升級</div>
    <div class="flex items-center gap-2 mb-1">
      <span class="bg-slate-100 text-slate-400 text-xs px-2 py-0.5 rounded shrink-0">沒用前</span>
      <span class="text-slate-500 text-xs">5 頁 emoji 拼貼，<br/>像 prototype 不像產品</span>
    </div>
    <div class="flex items-center gap-2 mb-2">
      <span class="bg-green-100 text-green-600 text-xs px-2 py-0.5 rounded shrink-0">用了後</span>
      <span class="text-slate-700 text-xs font-semibold">Material Icons 統一設計語言<br/>跨 5 頁一致，企業匯報品質</span>
    </div>
    <div class="text-slate-400 text-xs italic">從 prototype 升到可以對外展示</div>
  </div>

  <div class="border border-violet-100 rounded-2xl p-3">
    <div class="text-violet-500 font-bold text-sm mb-1">🔍 python-review</div>
    <div class="text-slate-500 text-xs mb-2">深度程式碼審查</div>
    <div class="flex items-center gap-2 mb-1">
      <span class="bg-slate-100 text-slate-400 text-xs px-2 py-0.5 rounded shrink-0">沒用前</span>
      <span class="text-slate-500 text-xs">以為沒問題<br/>（要跑起來才知道）</span>
    </div>
    <div class="flex items-center gap-2 mb-2">
      <span class="bg-violet-100 text-violet-600 text-xs px-2 py-0.5 rounded shrink-0">用了後</span>
      <span class="text-slate-700 text-xs font-semibold">找到 6 個潛在錯誤<br/>附修法，直接貼就能用</span>
    </div>
    <div class="text-slate-400 text-xs italic">不用跑也能找到 bug</div>
  </div>

  <div class="border border-amber-100 rounded-2xl p-3">
    <div class="text-amber-500 font-bold text-sm mb-1">🐦 canary</div>
    <div class="text-slate-500 text-xs mb-2">部署後效能監控</div>
    <div class="flex items-center gap-2 mb-1">
      <span class="bg-slate-100 text-slate-400 text-xs px-2 py-0.5 rounded shrink-0">沒用前</span>
      <span class="text-slate-500 text-xs">改了 1,239 行<br/>不知道效能有沒有退化</span>
    </div>
    <div class="flex items-center gap-2 mb-2">
      <span class="bg-amber-100 text-amber-600 text-xs px-2 py-0.5 rounded shrink-0">用了後</span>
      <span class="text-slate-700 text-xs font-semibold">5 頁比 baseline 快 34–61%<br/>確認 0 效能回歸</span>
    </div>
    <div class="text-slate-400 text-xs italic">benchmark baseline → canary 比對</div>
  </div>

  <div class="border border-orange-100 rounded-2xl p-3">
    <div class="text-orange-500 font-bold text-sm mb-1">📊 retro</div>
    <div class="text-slate-500 text-xs mb-2">工程回顧自動化</div>
    <div class="flex items-center gap-2 mb-1">
      <span class="bg-slate-100 text-slate-400 text-xs px-2 py-0.5 rounded shrink-0">沒用前</span>
      <span class="text-slate-500 text-xs">不知道 7 天做了什麼<br/>用了哪些工具</span>
    </div>
    <div class="flex items-center gap-2 mb-2">
      <span class="bg-orange-100 text-orange-600 text-xs px-2 py-0.5 rounded shrink-0">用了後</span>
      <span class="text-slate-700 text-xs font-semibold">17 commits、8 sessions<br/>skill usage 全自動彙整</span>
    </div>
    <div class="text-slate-400 text-xs italic">git log 就是原始資料，不需人工整理</div>
  </div>

</div>

---

## MVP → 專業品質的距離

<div class="mt-5 text-sm">
  <div class="grid grid-cols-7 gap-0 text-xs font-semibold text-slate-400 border-b border-slate-100 pb-2 mb-1">
    <div class="col-span-2">維度</div>
    <div class="col-span-2 text-center">MVP 前</div>
    <div class="col-span-1 text-center"></div>
    <div class="col-span-2 text-center text-indigo-500">Plugin 加持後</div>
  </div>
  <div class="space-y-2 text-xs">
    <div class="grid grid-cols-7 gap-0 items-center py-1.5 border-b border-slate-50">
      <div class="col-span-2 text-slate-600 font-medium">代碼品質</div>
      <div class="col-span-2 text-center text-slate-400">68 LOC，有死碼</div>
      <div class="col-span-1 text-center text-slate-300">→</div>
      <div class="col-span-2 text-center text-indigo-600 font-semibold">42 LOC，0 dead code</div>
    </div>
    <div class="grid grid-cols-7 gap-0 items-center py-1.5 border-b border-slate-50">
      <div class="col-span-2 text-slate-600 font-medium">安全掃描</div>
      <div class="col-span-2 text-center text-slate-400">從未掃描</div>
      <div class="col-span-1 text-center text-slate-300">→</div>
      <div class="col-span-2 text-center text-indigo-600 font-semibold">0 critical issues</div>
    </div>
    <div class="grid grid-cols-7 gap-0 items-center py-1.5 border-b border-slate-50">
      <div class="col-span-2 text-slate-600 font-medium">自動化測試</div>
      <div class="col-span-2 text-center text-slate-400">0 tests</div>
      <div class="col-span-1 text-center text-slate-300">→</div>
      <div class="col-span-2 text-center text-indigo-600 font-semibold">31 unit + 15 E2E，71% 覆蓋</div>
    </div>
    <div class="grid grid-cols-7 gap-0 items-center py-1.5 border-b border-slate-50">
      <div class="col-span-2 text-slate-600 font-medium">UX 審查</div>
      <div class="col-span-2 text-center text-slate-400">手動肉眼看</div>
      <div class="col-span-1 text-center text-slate-300">→</div>
      <div class="col-span-2 text-center text-indigo-600 font-semibold">2 HIGH 問題發現並修復</div>
    </div>
    <div class="grid grid-cols-7 gap-0 items-center py-1.5 border-b border-slate-50">
      <div class="col-span-2 text-slate-600 font-medium">瀏覽器 QA</div>
      <div class="col-span-2 text-center text-slate-400">未驗證</div>
      <div class="col-span-1 text-center text-slate-300">→</div>
      <div class="col-span-2 text-center text-indigo-600 font-semibold">5 頁全通過，95/100</div>
    </div>
    <div class="grid grid-cols-7 gap-0 items-center py-1.5">
      <div class="col-span-2 text-slate-600 font-medium">效能監控</div>
      <div class="col-span-2 text-center text-slate-400">不知道多快</div>
      <div class="col-span-1 text-center text-slate-300">→</div>
      <div class="col-span-2 text-center text-indigo-600 font-semibold">avg 51ms 基線，Canary 持續監控</div>
    </div>
  </div>
</div>

---

## 探索結論

<div class="grid grid-cols-3 gap-6 mt-8">
  <div class="border border-slate-100 rounded-2xl p-6">
    <div class="text-2xl mb-3">🚀</div>
    <div class="font-bold text-slate-800 mb-2">快速 Prototype</div>
    <div class="text-slate-500 text-sm">從零到可 demo 的速度，<br/>不受工具門檻卡住</div>
  </div>
  <div class="border border-slate-100 rounded-2xl p-6">
    <div class="text-2xl mb-3">🤖</div>
    <div class="font-bold text-slate-800 mb-2">AI 工具熟練度</div>
    <div class="text-slate-500 text-sm">不只會用，還知道<br/>邊界在哪、陷阱在哪</div>
  </div>
  <div class="border border-slate-100 rounded-2xl p-6">
    <div class="text-2xl mb-3">🎯</div>
    <div class="font-bold text-slate-800 mb-2">務實開發紀律</div>
    <div class="text-slate-500 text-sm">TDD、code review、<br/>文件同步更新</div>
  </div>
</div>

<div class="mt-10 text-center text-slate-600 text-lg italic">
  「AI 幫你跑得更快，方向和品質還是你的」
</div>
