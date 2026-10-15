# -*- coding: utf-8 -*-
"""Rewrite author page bodies to unified advisor / student templates (Markdown)."""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1] / "content" / "authors"

# focus / extra(学术 Markdown) / personal(个人 Markdown，放最后)
STUDENTS: dict[str, dict[str, str]] = {
    "chang-ya-xuan": {
        "focus": "事件相机弱光深度估计",
    },
    "dai-xue-yang": {
        "focus": "弱光深度估计",
        "personal": "- 来自河南省周口市",
    },
    "du-kun": {
        "focus": "单目深度估计",
        "personal": "- 1998 年生",
    },
    "guo-huan-huan": {
        "focus": "基于骨骼点的动作识别",
        "personal": "- 好好吃饭，好好睡觉，好好学习，好好运动",
    },
    "julianno": {
        "focus": "Monocular depth estimation in low-light environments",
        "extra": (
            "**学术背景**\n\n"
            "- 持有计算机科学硕士学位\n"
            "- 具备人工智能与深度学习基础\n"
            "- 致力于通过严谨研究推进相关方向的学术工作"
        ),
    },
    "li-peng-qin": {
        "focus": "深度估计",
        "extra": (
            "**学习与研究**\n\n"
            "- 本科毕业于西安理工大学计算机科学与技术专业\n"
            "- 目前通过文献调研与组会学习深入深度估计方向\n"
            "- 参与课题组相关基础工作"
        ),
    },
    "li-wen-gai": {
        "focus": "弱光图像增强与弱光深度估计",
        "extra": (
            "**已发表论文**\n\n"
            "1. 李文改，桂柯，肖照林，等. "
            "频域特征优化与截断采样的条件扩散模型弱光图像增强方法[J]. "
            "*中国图象图形学报*，2026, 31(9): 3352-3367.\n"
            "2. Li W, Xiao Z, Su H, et al. "
            "FEDD-Net: A Frequency Diagonal Feature Enhanced "
            "Dual-Branch Diffusion Network for Low-Light Image Enhancement[C]//"
            "*ICASSP 2026*. IEEE, 2026: 8757-8761."
        ),
    },
    "tian-yunxiang": {
        "focus": "智能体应用",
    },
    "tian-zhao-yang": {
        "focus": "事件相机深度估计",
        "extra": (
            "**学习与研究**\n\n"
            "- 本科主修计算机科学与技术\n"
            "- 掌握 Python、*PyTorch* 等工具\n"
            "- 目前处于文献阅读与入门阶段"
        ),
        "personal": "- 平时爱好羽毛球",
    },
    "wang-long-hao": {
        "focus": "基于骨骼的人体动作识别",
        "personal": (
            "> 宠辱不惊，闲看庭前花开花落；去留无意，漫随天外云卷云舒。"
        ),
    },
    "wang-xin-le": {
        "focus": "大模型应用",
    },
    "wang-yi": {
        "focus": "弱光图像增强",
        "extra": (
            "**技能与成果**\n\n"
            "- 熟练使用 *PyTorch* 开展深度学习实验\n"
            "- 熟悉图像算法设计与模型压缩优化\n"
            "- 先后发表期刊论文两篇，并拥有软件著作权"
        ),
        "personal": (
            "- 责任心强\n"
            "- 性格沉稳\n"
            "- 有良好执行力"
        ),
    },
    "xue-kai-xuan": {
        "focus": "弱光图像增强",
        "personal": "- 我是这个领域的专家",
    },
    "xue-yi-rui": {
        "focus": "智能体",
        "extra": (
            "**学习与研究**\n\n"
            "- 研究兴趣：人工智能、大语言模型与智能体\n"
            "- 具备 Python 编程基础\n"
            "- 关注深度学习与智能体开发的实践应用"
        ),
    },
    "zhai-qian-lin": {
        "focus": "动作识别",
    },
    "zhang-heng-chang": {
        "focus": "智能体",
        "personal": "- 热爱生活",
    },
    "zhao-guan-zheng": {
        "focus": "大模型与智能体",
        "personal": "- 性格开朗活泼",
    },
    "zhou-guang-bin": {
        "focus": "弱光增强与单目深度估计",
        "personal": (
            "- 爱好：羽毛球 / 乒乓球 / 篮球、骑行、美食\n"
            "- MBTI：*ENTJ-A*"
        ),
    },
    "zhou-he-xin": {
        "focus": "大模型应用",
    },
}

ADVISORS: dict[str, str] = {
    "admin": (
        "**肖照林**，工学博士，教授，博士生导师，现任副院长。\n\n"
        "**研究方向：** 计算机视觉、计算摄影与人工智能  \n"
        "主要从事光场成像分析及 3D 场景重建理论研究，"
        "参与研制国产自主知识产权多型光场成像系统。\n\n"
        "**学术**\n\n"
        "- 主持国家自然科学基金 3 项及省级以上课题多项\n"
        "- 以第一/责任作者发表学术论文 60 余篇（含 *CVPR*、*AAAI* 等顶刊顶会）\n"
        "- 授权发明专利 15 项\n"
        "- 兼任 CCF 高级会员、IEEE 会员及多个专委会委员\n\n"
        "**教学**\n\n"
        "- 主讲《软件工程导论》等多门课程\n"
        "- 曾获“优秀青年教师”等荣誉\n"
        "- 指导学生获“互联网+”金奖等竞赛奖励 30 余项"
    ),
    "su-haonan": (
        "**苏浩楠**，西安理工大学计算机科学与技术学院教师。\n\n"
        "**研究方向：** 计算机视觉与计算摄影"
    ),
}

DEGREE_BY_ROLE = {
    "研一": ("硕士研究生", "研一"),
    "研二": ("硕士研究生", "研二"),
    "研三": ("硕士研究生", "研三"),
    "博一": ("博士研究生", "博一"),
    "博二": ("博士研究生", "博二"),
    "博三": ("博士研究生", "博三"),
}


def split_fm(text: str) -> tuple[str, str]:
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise SystemExit("missing front matter")
    return parts[1], parts[2]


def set_yaml_line(fm: str, key: str, value: str, *, quoted: bool = True) -> str:
    q = f"\"{value}\"" if quoted else value
    pattern = rf"(^{re.escape(key)}:\s*)([^\n]*)"
    out, n = re.subn(pattern, rf"\1{q}", fm, count=1, flags=re.M)
    if n != 1:
        raise SystemExit(f"failed to set {key}")
    return out


def student_body(
    name: str,
    role: str,
    focus: str,
    extra: str | None,
    personal: str | None,
) -> str:
    degree, grade = DEGREE_BY_ROLE[role]
    lines = [
        f"**{name}**，西安理工大学计算机科学与技术学院**{degree}**（{grade}），导师：肖照林教授。",
        "",
        f"**研究方向：** {focus}",
    ]
    if extra:
        lines.extend(["", extra])
    if personal:
        lines.extend(["", "**个人**", "", personal])
    return "\n".join(lines) + "\n"


def main() -> None:
    for d in sorted(ROOT.iterdir()):
        f = d / "_index.md"
        if not f.exists():
            continue
        text = f.read_text(encoding="utf-8")
        fm, _body = split_fm(text)
        title_m = re.search(r"^title:\s*(.+)$", fm, re.M)
        role_m = re.search(r"^role:\s*[\"']?(.*?)[\"']?\s*$", fm, re.M)
        if not title_m or not role_m:
            raise SystemExit(f"missing title/role in {d.name}")
        name = title_m.group(1).strip()
        role = role_m.group(1).strip()

        if d.name in ADVISORS:
            body = ADVISORS[d.name] + "\n"
        elif d.name in STUDENTS:
            info = STUDENTS[d.name]
            if role not in DEGREE_BY_ROLE:
                raise SystemExit(f"{d.name}: unexpected role {role!r}")
            focus = info["focus"]
            body = student_body(
                name, role, focus, info.get("extra"), info.get("personal")
            )
            fm = set_yaml_line(fm, "research_focus", focus)
            fm = set_yaml_line(fm, "bio", f"研究方向为{focus}。")
        else:
            raise SystemExit(f"unlisted author folder: {d.name}")

        f.write_text(f"---{fm}---\n\n{body}", encoding="utf-8", newline="\n")
        print("updated", d.name)


if __name__ == "__main__":
    main()
