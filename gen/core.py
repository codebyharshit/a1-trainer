import hashlib, random, re

R = random.Random(42)
QUESTIONS = []


def seg(spec):
    """'Ich#S / {kaufe}#V / einen Apfel#AKK' -> [[text, label], ...]"""
    out = []
    for part in spec.split(" / "):
        if "#" in part:
            t, l = part.rsplit("#", 1)
        else:
            t, l = part, ""
        out.append([t, l])
    return out


def add(topic, segs, options, rule, why=None, prompt=None, note=None, mode="gap"):
    """segs: list of [text,label]; exactly one text contains {answer} for gap questions.
    options: list, correct answer first. why: {wrong_option: explanation}."""
    if isinstance(segs, str):
        segs = seg(segs)
    full = []
    p = None
    for t, l in segs:
        m = re.search(r"\{(.*?)\}", t)
        if m and mode == "gap":
            p = True
        full.append([re.sub(r"[{}]", "", t), l])
    if mode == "gap" and prompt is None:
        prompt = " ".join(re.sub(r"\{.*?\}", "___", t) for t, _ in segs)
        prompt = re.sub(r"\s+([.?!,])", r"\1", prompt)
    opts = []
    for o in options:
        if o not in opts:
            opts.append(o)
    qid = hashlib.md5((topic + "|" + prompt + "|" + opts[0]).encode()).hexdigest()[:10]
    q = {"id": qid, "t": topic, "p": prompt, "o": opts, "w": rule, "s": full}
    if why:
        q["d"] = {k: v for k, v in why.items() if k in opts and k != opts[0]}
    if note:
        q["n"] = note
    QUESTIONS.append(q)
    return q


def choose(topic, prompt, correct_spec, wrong, rule, why=None, note=None):
    segs = seg(correct_spec)
    correct = " ".join(t for t, _ in segs)
    correct = re.sub(r"\s+([.?!,])", r"\1", correct)
    return add(topic, segs, [correct] + wrong, rule, why, prompt=prompt, note=note, mode="choose")


def pick(lst, k):
    return R.sample(lst, min(k, len(lst)))
