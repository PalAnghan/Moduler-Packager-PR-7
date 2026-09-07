<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:FF0080,25:FF8C00,50:39FF14,75:00D9FF,100:B026FF&height=220&section=header&text=Moduler%20%26%20Packager&fontSize=46&fontColor=ffffff&fontAlignY=38&animation=twinkling&desc=%3C%3C%20Python%20Multi-Utility%20Toolkit%20%3E%3E&descAlignY=58&descSize=18&descColor=ffffff" width="100%"/>

<img src="https://user-images.githubusercontent.com/74038190/213910845-af37a709-8995-40d6-be59-724526e3c3d7.gif" width="100%" height="4">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=24&duration=2200&pause=700&color=FF0080,39FF14,00D9FF&center=true&vCenter=true&multiline=true&width=700&height=90&lines=%F0%9F%9A%80+datetime+%E2%80%A2+math+%E2%80%A2+random+%E2%80%A2+uuid;%F0%9F%A7%A9+custom+modules+%2B+packages;%F0%9F%94%8D+dir()+%3D+explore+everything+LIVE" alt="Typing SVG"/>

<br/>

<img src="https://media.giphy.com/media/L1R1tvL9vlrxC/giphy.gif" width="90"/>&nbsp;&nbsp;
<img src="https://media.giphy.com/media/QTfX9eTsWtEuY/giphy.gif" width="90"/>&nbsp;&nbsp;
<img src="https://media.giphy.com/media/xUOxf6RRP9Cf2rjkla/giphy.gif" width="90"/>

<br/><br/>

![visitors](https://visitor-badge.laobi.icu/badge?page_id=palanghan.moduler-packager-pr-7&style=for-the-badge&color=FF0080)
![Python](https://img.shields.io/badge/PYTHON-3.12-39FF14?style=for-the-badge&logo=python&logoColor=black&labelColor=000000)
![Status](https://img.shields.io/badge/STATUS-ONLINE-00D9FF?style=for-the-badge&labelColor=000000)
![Vibes](https://img.shields.io/badge/VIBES-IMMACULATE-B026FF?style=for-the-badge&labelColor=000000)

<img src="https://user-images.githubusercontent.com/74038190/213910845-af37a709-8995-40d6-be59-724526e3c3d7.gif" width="100%" height="4">

</div>

<div align="center">

```
█▓▒░ "Quality is our Motto." — Shaping "skills" for "scaling" higher...!!! ░▒▓█
```

</div>

<br/>

## 🛸 Overview

<img align="right" width="200" src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif"/>

`Moduler & Packager` is a menu-driven **Python Multi-Utility Toolkit** engineered to show off Python's modular system top to bottom — built-in modules, hand-rolled custom modules, and real packages, wired together behind one slick interface.

It runs on `datetime`, `time`, `math`, `random`, and `uuid` from the standard library, then layers a custom `utilities` package on top — file ops, calculations, identifiers, and more — every piece inspectable **live** through `dir()`.

<br clear="right"/>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

## 🎯 Objective

<table>
<tr>
<td width="25%" align="center">⚡<br><b>Built-in Power</b><br><sub><code>datetime</code> <code>time</code> <code>math</code><br><code>random</code> <code>uuid</code></sub></td>
<td width="25%" align="center">🧩<br><b>Custom Packages</b><br><sub><code>interface/</code> +<br><code>utilities/</code> w/ <code>__init__.py</code></sub></td>
<td width="25%" align="center">🛡️<br><b>Clean Scripts</b><br><sub><code>__name__ == "__main__"</code><br>on every module</sub></td>
<td width="25%" align="center">🔬<br><b>Live Exploration</b><br><sub>runtime <code>dir()</code><br>inspection</sub></td>
</tr>
</table>

## ✨ Features

<details open>
<summary><b>⏰ Datetime & Time Module</b></summary>
<br>

![](https://progress-bar.dev/100/?title=complete&color=39FF14&width=300)

- Display current date & time
- Diff between two dates/times
- Custom `strftime` formatting
- Stopwatch + countdown timer

</details>

<details open>
<summary><b>🧮 Math Module</b></summary>
<br>

![](https://progress-bar.dev/100/?title=complete&color=00D9FF&width=300)

- Trigonometry, factorials, logarithms
- Compound interest calculator
- Geometric shape area solver

</details>

<details open>
<summary><b>🎲 Random + 🆔 UUID Modules</b></summary>
<br>

![](https://progress-bar.dev/100/?title=complete&color=FF0080&width=300)

- Random numbers, lists, secure passwords, OTPs
- Dataset sampling & simple game simulations
- UUID4-based unique identifiers

</details>

<details open>
<summary><b>🗂️ Custom File Ops + 🔍 Module Explorer</b></summary>
<br>

![](https://progress-bar.dev/100/?title=complete&color=B026FF&width=300)

- Create / write / read / append via reusable functions
- Explore attributes of **any** module live with `dir()`

</details>

<img src="https://user-images.githubusercontent.com/74038190/213910845-af37a709-8995-40d6-be59-724526e3c3d7.gif" width="100%" height="4">

## 🗂 File Structure

```mermaid
flowchart TD
    A(["🚀 main.py"]) --> B["📦 interface/"]
    B --> C["menu.py"]
    A --> D["📦 utilities/"]
    D --> E["date_tools.py"]
    D --> F["calculation_tools.py"]
    D --> G["random_tools.py"]
    D --> H["identifier_tools.py"]
    D --> I["storage_tools.py"]
    D --> J["explore_tools.py"]
    A --> K["📁 files/"]

    style A fill:#FF0080,color:#fff
    style B fill:#39FF14,color:#000
    style D fill:#00D9FF,color:#000
    style K fill:#B026FF,color:#fff
```

<details>
<summary>📁 raw tree</summary>

```
Python_MultiUtility/
├── main.py
├── files/
│   ├── ex.txt
│   └── sample.txt
├── interface/
│   ├── __init__.py
│   └── menu.py
└── utilities/
    ├── __init__.py
    ├── calculation_tools.py
    ├── date_tools.py
    ├── explore_tools.py
    ├── identifier_tools.py
    ├── random_tools.py
    └── storage_tools.py
```

</details>

## ⚙️ Installation

```bash
git clone https://github.com/PalAnghan/Moduler-Packager-PR-7.git
cd Moduler-Packager-PR-7/Python_MultiUtility
python main.py
```

> 🟢 Zero dependencies — pure standard library.

## 🚀 Usage

```
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
```

## 🎬 Demo Video

<div align="center">

<img src="https://media.giphy.com/media/3o7bu3XilJ5BOiSGic/giphy.gif" width="220"/>

**🚧 Demo video incoming — will be embedded right here 🚧**

</div>

## 📟 Sample Run

```diff
+ Enter your choice: 1 → Display current date and time
+ Current Date and Time: 2025-01-04 10:15:30

+ Enter your choice: 2 → Calculate Factorial
+ Enter a number: 5
+ Factorial: 120

+ Enter module name to explore: math
+ ['acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh', 'ceil', 'comb', ...]
```

## 📦 Deliverables & Evaluation

| 📦 Deliverables | 📊 Evaluated On |
|---|---|
| Menu-driven Python source | Functionality |
| Custom modules & packages | Code structure & modularity |
| Sample outputs (logs, IDs, reports) | Documentation |
| — | Innovation |

<img src="https://user-images.githubusercontent.com/74038190/213910845-af37a709-8995-40d6-be59-724526e3c3d7.gif" width="100%" height="4">

## 👤 Author

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=2500&pause=900&color=39FF14,00D9FF,FF0080&center=true&vCenter=true&width=500&lines=Pal+Anghan;Final-year+BCA+%7C+AI-ML+in+progress" alt="Author Typing SVG"/>

<br/>

[![Gmail](https://img.shields.io/badge/-palanghan8@gmail.com-000000?style=for-the-badge&logo=gmail&logoColor=EA4335)](mailto:palanghan8@gmail.com)
[![LinkedIn](https://img.shields.io/badge/-pal--anghan-000000?style=for-the-badge&logo=linkedin&logoColor=0A66C2)](https://linkedin.com/in/pal-anghan)
[![GitHub](https://img.shields.io/badge/-PalAnghan-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/PalAnghan)

</div>

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:B026FF,25:00D9FF,50:39FF14,75:FF8C00,100:FF0080&height=150&section=footer&animation=twinkling" width="100%"/>

<sub>⭐ if this toolkit helped you — it keeps the neon lights on ⭐</sub>

</div>
