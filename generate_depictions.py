#!/usr/bin/env python3
import json
from pathlib import Path

DATA = {
 'com.hua.topgauge': ('TopGauge', '1.8.18.1', '横竖屏悬浮监测窗，支持 CPU 使用率、SpringBoard 内存占用等指标的显隐与排序。\n\n可自定义小窗外观，支持拖动和长按固定。', '保留小窗外观设置，移除双击大窗及其专属设置；合并重复滑条创建和布局代码。插件与设置组件改为仅 arm64e。'),
 'com.hua.jikan': ('Jikan', '1.1.23.1', '充电信息胶囊：显示预计充满时间、电量、电流、温度、功率等信息，并保留音乐相关功能。\n\n充电预估使用简易算法，并考虑温度与无线充电修正。', '清理不再使用的电源辅助服务、启动配置、专用协议及维护脚本；移除成功操作的开发诊断与无引用本地化文本，保留失败反馈。沿用 1.1.22 的充电预估算法。'),
 'com.hua.screencorehelper': ('ScreenCore Helper', '0.5.45', 'ScreenCore 1.1.6 配套增强，0.5.45 清理稳定版。RootHide 单 arm64e（thinUnified），沿用原注入 Filter。\n\n以用户实测通过的 0.5.44 拖动修复为基线，提供 ARC 菜单背景、分屏、停靠、容量管理、比例与相关手势增强，并保留既有设置和 WeType 收键盘机制。\n\nARC 矩形角半径为短边的 35%，毛玻璃 visualSide 为 0.9。\n\n已知问题：分屏转全屏时 WeType 键盘退场残留、横屏相机方向尚未解决。已停止的窗口模式不包含在本版本。\n\n稳定版不代表 0.5.45 所有功能已重新完成真机验收。保留既有 Theos/RootHide 签名机制；Apple codesign 严格校验未通过，嵌入页哈希已核验，设备信任、加载与运行仍待设备验证。', '以用户实测通过的 0.5.44 为稳定基线。保留该版对 0.5.27 新增普通窗口重排与按住拖动跨中轴冲突的修复：拖动 owner/token 及终态归栏控制不变，避免拖动过程中被普通重排争抢。\n\n保留 ARC 矩形 35% 圆角、visualSide 0.9 毛玻璃，以及原有分屏、停靠、容量限制与恢复接力、方向与比例、配置和 WeType 收键盘功能。\n\n本次真实 Mac 重新构建：删除生产诊断日志与状态写盘、恒 NO 的 Reject 空壳、零写入 handoffDepth 对应的纯透传 live hook、无读取 generation 与无消费者 HomeDock helpers。生产源码净减少 2,777 字节，动态库减少 16,784 字节。有效准入、失败清理、0544 拖动 token、原 Filter 与四个生产编译单元保留。\n\n验证包括真实 Mac 构建、源码差异白名单、host tests 与嵌入页哈希；不代表 0.5.45 全部功能新增真机验收。沿用既有 RootHide 签名机制，Apple codesign 严格校验未通过；未声称 Apple-valid 或设备已重测。\n\n已知问题未解决：split→fullscreen 的 WeType 退场残留、横屏相机方向。已停止的窗口模式不包含。\n\n### 0.5.33（历史记录）\n\n用户指定 0.5.33 为稳定版，发布已交付的 RootHide 单 arm64e 原包，未重新编译。稳定标记不代表新增真机验收。\n\n首次停靠中心 25%；普通归栏默认 0.6s、缩放前置 0.22s、轻 spring 默认 0.92；触发区域竖屏 35%、横屏 20%。目标关闭 0.22s，其余无动画。\n\nHelper 自带微信扩展收键盘：开关 on 才发，off 不发；忽略 delay。宿主无需注入，但扩展需允许。\n\n已知问题：分屏转全屏时键盘退场动画残留尚未解决。0.5.34 实验未解决用户反馈的问题，不发布。'),
 'com.hua.wetypecleansix': ('WeTypeCleanSix', '0.2.0.1', '六按钮快捷栏：剪切、全选、复制、粘贴、历史、收起。支持无选区时复制或剪切全文、按键震动、键盘外侧圆角及隐藏候选高亮。\n\n历史入口需要兼容的剪贴板历史插件。', '新增固定启用的丝滑光标，无新增设置项。采用 iOS 15 / 16 光标实现，不含 iOS 17 分支；原有六按钮功能保持不变。'),
 'com.hua.systemboxappearanceaddon': ('SystemBox Appearance Addon', '0.3.4.1', 'SystemBox 外观配套扩展，支持深浅图标切换、菜单操作和图标缓存批量刷新，保留配置迁移及文件夹图标叠层转场保护。\n\n适配记录指向 SystemBox 1.5-8end。', '改为仅 arm64e，继续采用单 dylib；清理无用集合、计数器、函数指针和冗余数据，复用同次配置读取。原有功能及初始化顺序保留。\n\n本版本尚无真机视觉验收记录。'),
}
BASE = 'https://huafuquan.github.io/hua/depictions/'
root = Path('public')
out = root / 'depictions'
out.mkdir(parents=True, exist_ok=True)
for package, (name, version, description, changes) in DATA.items():
    def tab(title, text):
        return {'tabname': title, 'class': 'DepictionStackView', 'views': [{'class': 'DepictionMarkdownView', 'markdown': text, 'useSpacing': True}]}
    depiction = {'class': 'DepictionTabView', 'tabs': [tab('详情', description), tab('更新日志', '### ' + version + ('\n\n' if package == 'com.hua.screencorehelper' else '\n\n修复软件包目录权限，恢复原始归档的权限、所有权和链接。插件功能与二进制不变。\n\n') + changes)]}
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
