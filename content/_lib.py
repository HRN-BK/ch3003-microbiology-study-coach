"""Authoring helpers. Each family module calls unit(), q(), v(), fc(), we().
build.py imports the family modules in order and reads the global lists below."""
import textwrap

UNITS, QS, VOC, FC, WE = [], [], [], [], []


def _clean(s):
    return textwrap.dedent(s).strip("\n") if isinstance(s, str) else s


def unit(id, title, priority, difficulty, minutes, source, hookVi, predict, lesson, extension, keyCards, traps, prereq=()):
    """lesson / extension: list of (heading, body). keyCards: list of (title, bodyEn, glossVi).
    predict: (stem, options, answer, explanationVi)."""
    UNITS.append({
        "id": id, "title": title, "priority": priority, "difficulty": difficulty, "minutes": minutes,
        "source": source, "prereq": list(prereq), "hookVi": _clean(hookVi),
        "predictQuestion": {"stem": _clean(predict[0]), "options": list(predict[1]), "answer": predict[2], "explanation": _clean(predict[3])},
        "lesson": [{"h": h, "body": _clean(b)} for h, b in lesson],
        "extension": [{"h": h, "body": _clean(b)} for h, b in extension],
        "keyCards": [{"title": t, "bodyEn": _clean(b), "glossVi": _clean(g)} for t, b, g in keyCards],
        "traps": list(traps),
    })


def q(unit, type, difficulty, stem, options, answer, explanation, notes=None, vocab=(), trap=None, pool="learn", src="", steps=None):
    QS.append({
        "unit": unit, "type": type, "difficulty": difficulty, "stem": _clean(stem), "options": list(options),
        "answer": answer, "explanation": _clean(explanation),
        "distractorNotes": list(notes) if notes else ["", "", "", ""],
        "vocab": list(vocab), "trap": trap, "pool": pool, "source": src,
        **({"steps": list(steps)} if steps else {}),
    })


def v(unit, term, vi, definition, example, aliases=()):
    VOC.append({"unit": unit, "term": term, "vi": vi, "def": definition, "example": example, "aliases": list(aliases)})


def fc(unit, kind, front, back):
    FC.append({"unit": unit, "kind": kind, "front": _clean(front), "back": _clean(back)})


def we(id, unit, title, problem, steps, finalAnswer, explanationVi, fade=None):
    """steps: list of dicts {prompt, answer, input('number'|'choice'|'text'), hint?, choices?}"""
    n = len(steps)
    WE.append({
        "id": id, "unit": unit, "title": title, "problem": _clean(problem), "steps": steps,
        "finalAnswer": _clean(finalAnswer), "explanationVi": _clean(explanationVi),
        "fadeLevels": fade or {"0": [], "1": [n - 1], "2": list(range(max(0, n - 3), n)), "3": "all"},
    })


def S(prompt, answer, input="number", hint=None, choices=None):
    d = {"prompt": prompt, "answer": answer, "input": input}
    if hint: d["hint"] = hint
    if choices: d["choices"] = choices
    return d
