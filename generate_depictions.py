#!/usr/bin/env python3
import json
from pathlib import Path

DATA = {
 'com.hua.topgauge': ('TopGauge', '1.8.18', '横竖屏悬浮监测窗，支持 CPU 使用率、SpringBoard 内存占用等指标的显隐与排序。\n\n可自定义小窗外观，支持拖动和长按固定。', '保留小窗外观设置，移除双击大窗及其专属设置；合并重复滑条创建和布局代码。插件与设置组件改为仅 arm64e。'),
 'com.hua.jikan': ('Jikan', '1.1.23', '充电信息胶囊：显示预计充满时间、电量、电流、温度、功率等信息，并保留音乐相关功能。\n\n充电预估使用简易算法，并考虑温度与无线充电修正。', '清理不再使用的电源辅助服务、启动配置、专用协议及维护脚本；移除成功操作的开发诊断与无引用本地化文本，保留失败反馈。沿用 1.1.22 的充电预估算法。'),
 'com.hua.screencorehelper': ('ScreenCore Helper', '0.5.17', 'ScreenCore 1.1.6 配套增强。\n\n提供 ARC 菜单背景、背景强度调节与扩散动画，保留分屏、停靠及相关手势增强。', '减少 ARC 背景的重复几何更新、移动和属性设置；扩散动画结束时按最新圆角半径同步最终状态。模糊效果、动画时长、手势、分屏和停靠策略保持不变。\n\n长期使用后的 ARC 掉帧是否彻底修复尚未证实。'),
 'com.hua.wetypecleansix': ('WeTypeCleanSix', '0.2.0', '六按钮快捷栏：剪切、全选、复制、粘贴、历史、收起。支持无选区时复制或剪切全文、按键震动、键盘外侧圆角及隐藏候选高亮。\n\n历史入口需要兼容的剪贴板历史插件。', '新增固定启用的丝滑光标，无新增设置项。采用 iOS 15 / 16 光标实现，不含 iOS 17 分支；原有六按钮功能保持不变。'),
 'com.hua.systemboxappearanceaddon': ('SystemBox Appearance Addon', '0.3.4', 'SystemBox 外观配套扩展，支持深浅图标切换、菜单操作和图标缓存批量刷新，保留配置迁移及文件夹图标叠层转场保护。\n\n适配记录指向 SystemBox 1.5-8end。', '改为仅 arm64e，继续采用单 dylib；清理无用集合、计数器、函数指针和冗余数据，复用同次配置读取。原有功能及初始化顺序保留。\n\n本版本尚无真机视觉验收记录。'),
}
BASE = 'https://huafuquan.github.io/hua/depictions/'
root = Path('public')
out = root / 'depictions'
out.mkdir(parents=True, exist_ok=True)
for package, (name, version, description, changes) in DATA.items():
    def tab(title, text):
        return {'tabname': title, 'class': 'DepictionStackView', 'views': [{'class': 'DepictionMarkdownView', 'markdown': text, 'useSpacing': True}]}
    depiction = {'class': 'DepictionTabView', 'tabs': [tab('详情', description), tab('更新日志', '### ' + version + '\n\n' + changes)]}
    (out / (package + '.json')).write_text(json.dumps(depiction, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
path = root / 'Packages'
paragraphs = path.read_text(encoding='utf-8').strip().split('\n\n')
seen = set()
for i, paragraph in enumerate(paragraphs):
    package = next((line[9:].strip() for line in paragraph.splitlines() if line.startswith('Package: ')), '')
    if package in DATA:
        paragraphs[i] = paragraph + '\nSileoDepiction: ' + BASE + package + '.json'
        seen.add(package)
if seen != set(DATA):
    raise SystemExit('Package mismatch: ' + repr(set(DATA) - seen))
path.write_text('\n\n'.join(paragraphs) + '\n\n', encoding='utf-8')
