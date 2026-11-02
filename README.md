# hua

iOS 越狱 APT 软件源，地址：https://huafuquan.github.io/hua/

在 Sileo / Zebra 中添加上述地址即可。以下均为作者指定的当前稳定版，架构 `iphoneos-arm64e`（RootHide）。完整更新记录见 [CHANGELOG.md](CHANGELOG.md)。

| 插件 | 稳定版 |
|---|---|
| TopGauge | 1.8.18+minimal.3 |
| Jikan | 1.1.23 |
| ScreenCore Helper（适配 ScreenCore 1.1.6） | 0.5.17-arc-performance-test |
| WeTypeCleanSix（六按钮快捷栏·插件版） | 0.2.0-lite-smooth-test |
| SystemBox Appearance Addon | 0.3.4-arm64e-minimal |

## 插件功能

### TopGauge
横竖屏悬浮监测窗：CPU 使用率、SpringBoard 内存占用等指标可显隐、排序；小窗外观自定义、拖动、长按固定。SpringBoard 内存采用 Phys footprint 口径。

### Jikan
桌面充电信息胶囊：显示预计充满时间，以及电量、电流、温度、功率等信息，保留音乐相关功能。充电预估使用 TopGauge 简易算法（剩余容量 / 电流，含温度与无线充电修正）。

### ScreenCore Helper
ScreenCore 1.1.6 配套增强：ARC 菜单背景、背景强度调节与扩散动画，保留分屏、停靠及相关手势增强。

### WeTypeCleanSix（六按钮快捷栏·插件版）
微信输入法键盘六按钮快捷栏：剪切、全选、复制、粘贴、历史、收起；无选区时复制 / 剪切全文，按键震动；保留键帽圆角、隐藏候选高亮、键盘外侧圆角。历史入口需要兼容的剪贴板历史插件。内置固定启用的丝滑光标（iOS 15 / 16）。

### SystemBox Appearance Addon
SystemBox 外观配套扩展：深浅图标切换、四菜单操作、图标缓存批量刷新，保留默认配置迁移与文件夹首图标叠层转场保护。适配 SystemBox 1.5-8end。
