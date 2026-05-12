import json
from pathlib import Path

# --- CONFIGURATION (Fixed Data) ---
CONFIG = {
    "output": "soham_profile.svg",
    "canvas": {
        "width": 1000,
        "height": 1150, 
        "radius": 20,
        "background": "#0d1117",
        "font_family": "Consolas, 'Courier New', monospace",
        "font_size": 14,
        "line_height": 16
    },
    "layout": {
        "left_x": 60,
        "top_y": 50
    },
    "colors": {
        "background": "#0d1117",
        "ascii": "#89929b",
        "text": "#ecf2f8",
        "name": "#7ce38b",
        "accent": "#faa356",
        "comment": "#484f58",
        "label": "#77bdfb"
    },
    "lines": [
        # --- ASCII ART SECTION ---
        {"spans": [{"text": "                                                   ;\" ::_\"I.`:                                     ", "fill": "ascii"}]},
        {"spans": [{"text": "                                               ';+l>1{[{??~]]^:\".                                 ", "fill": "ascii"}]},
        {"spans": [{"text": "                                             '_~xcXvYQOUwXYr_)-!!.'                               ", "fill": "ascii"}]},
        {"spans": [{"text": "                                            :frxxdW8&8%8%%mmdb||<+\"                               ", "fill": "ascii"}]},
        {"spans": [{"text": "                                          .!}thW&#wXxtxwpa&8%%#r\\(>;.                             ", "fill": "ascii"}]},
        {"spans": [{"text": "                                        .+<>(aCL+l;,l:!l~}JqM8BBz/r[i'                            ", "fill": "ascii"}]},
        {"spans": [{"text": "                                       '!l<\\wJ' .iLakoaati[|Ob&BaJ0j-^                            ", "fill": "ascii"}]},
        {"spans": [{"text": "                                       .I~Yhv<^.>pn\"x##*d\\}{Ykp%Zjt{^                             ", "fill": "ascii"}]},
        {"spans": [{"text": "                                         .,{n1+>hhhBBBk*dX\\rmCQ#OX~\"                              ", "fill": "ascii"}]},
        {"spans": [{"text": "                                           'l-[?\\/vL#8*dkadhpLwwx:^,.                             ", "fill": "ascii"}]},
        {"spans": [{"text": "                                             ^^:l>\\LXJOQYfn\\]|-!'                                 ", "fill": "ascii"}]},
        {"spans": [{"text": "                                                 ^)<(|}[(,.`..                                    ", "fill": "ascii"}]},
        {"spans": [{"text": "                                                .}+[>{!<~~.                                       ", "fill": "ascii"}]},
        {"spans": [{"text": "                                               .)>,{i[:,!I\\                                       ", "fill": "ascii"}]},
        {"spans": [{"text": "                                              .~!>+`i+:~.<'+^                                     ", "fill": "ascii"}]},
        {"spans": [{"text": "                                              ]I- _'!,!-.\"-.['                                    ", "fill": "ascii"}]},
        {"spans": [{"text": "                                             _^>'\"';'! ~'? ;! ~:                                   ", "fill": "ascii"}]},
        {"spans": [{"text": "                                            Il:i ;:'i _ ]. i\".+`                                  ", "fill": "ascii"}]},
        {"spans": [{"text": "                                           >!`} .- '! + ^l '-  ~l                                 ", "fill": "ascii"}]},
        {"spans": [{"text": "                                          Il.+. \"< ;; ~ '!  \"_  >;.                               ", "fill": "ascii"}]},
        {"spans": [{"text": "                                         .- ,l  }  _` <. <.  :!  <!                               ", "fill": "ascii"}]},
        {"spans": [{"text": "                                        ,? ']  ^+  }  l^ II  .~   ;!                              ", "fill": "ascii"}]},
        {"spans": [{"text": "                                       ^< .[   !`  }  :\"  {   .)   !>                             ", "fill": "ascii"}]},
        {"spans": [{"text": "                                      .}' !\"   i'  }  ;,  i,   `<   \"+                            ", "fill": "ascii"}]},
        {"spans": [{"text": "                                     '?  .+   '<   [  ;\"   ~    i\"   :+                           ", "fill": "ascii"}]},
        {"spans": [{"text": "                                     ~` .|    i:  \"+  :,  .!^    [.   .]                          ", "fill": "ascii"}]},
        {"spans": [{"text": "                                    }\"  ~     {   i,  \"l   I,    .]    \"+                         ", "fill": "ascii"}]},
        {"spans": [{"text": "                                   ~'  \"i    Il   +   '~   '~     :!     )'                       ", "fill": "ascii"}]},
        {"spans": [{"text": "                                  il   [     +    +    _    -      _     .~'                      ", "fill": "ascii"}]},
        {"spans": [{"text": "                                 >I  .].    ^!    +    _    `_      )      )`                     ", "fill": "ascii"}]},
        {"spans": [{"text": "                                Il   ;;     \"I    +    -     ?      '~      >,                    ", "fill": "ascii"}]},
        {"spans": [{"text": "                               ,+    -      _'   .<    _.    ,l      !\"      ?^                   ", "fill": "ascii"}]},
        {"spans": [{"text": "                              ;~    1       ]   .\"l   .!;-QhLC\\..     {.      !l                  ", "fill": "ascii"}]},
        {"spans": [{"text": "                             '~    !,      _^,[/-|f\\)[\\t])!?}(([tjfxrfxc;.     ~\"                 ", "fill": "ascii"}]},
        {"spans": [{"text": "                            ')    ^<    ':+I{:;_}:<,?t?}j-<~_I\\][1_}/-))QXwZzl. !>                ", "fill": "ascii"}]},
        {"spans": [{"text": "                           `+     ]` +x{[]:~;-`!\"I~_!-\\+++~}~+?}?)+[-fLYcCXCUcvt:!;               ", "fill": "ascii"}]},
        {"spans": [{"text": "                           -^    _(nr|[+l<l;<><,<;<?i)1?_}_{~[?<?}\\t|)JzcYYvYt1\\n/C}.             ", "fill": "ascii"}]},
        {"spans": [{"text": "                          {.    +x~{)f_[!'l[+\"~]-;[(_1[_~)}[{]\\\\|-]]umrmmxcUvt/(\\]{xO             ", "fill": "ascii"}]},
        {"spans": [{"text": "                         <^    {t{{}]]]]i!-l>-~][<{\\t|{_~+?}UpzOvf/[\\vQwLqYO\\[)ttj{?1J;           ", "fill": "ascii"}]},
        {"spans": [{"text": "                        ~;   .[/}]>}]](>[??~l1-~(jCx([{+~{z~   ,)j/v|uXwUuYki]_/\\/-ii_{`          ", "fill": "ascii"}]},
        {"spans": [{"text": "                       ~,   !{]i-<~?1rt{-i}+>]))(|_+[/1/[:       .<t\\/CvzXcL_~~?1[__<,(1.         ", "fill": "ascii"}]},
        {"spans": [{"text": "                      ;l  :1<{>-<~!?u-?+<}~<1]{,.  ...   `;'t`     'nn)zu/tj{>-<+~}1]\")|)'        ", "fill": "ascii"}]},
        {"spans": [{"text": "                     I~..}}]+?i~-~lrt(l:^''.           ?-\\fff1       >|Y/(}//:}+__1-_-{x-1.       ", "fill": "ascii"}]},
        {"spans": [{"text": "                    ;i'-}{<i_~?i+<}-j,                ,xUnjr[-        ^xr)}+f1i_]?|xux)(-tx-:.    ", "fill": "ascii"}]},
        {"spans": [{"text": "                    --\\]_lI?!l_l]>!>(;                  '|)||\\`        }1<_I]Xv){]}+)][]_<\\\\/trx{. ", "fill": "ascii"}]},
        {"spans": [{"text": "                  ;f?_-ll-!l-1[ti!>_):                    '{}?|)^     ^>1[~I{|n]11|~\\}i<\\)(\\r|/Yb< ", "fill": "ascii"}]},
        {"spans": [{"text": "               'i(_-<<_-_i}1! {-!i<}1                      .+]>~1x;-1_-I}1[?_(uj/]|)\\}[|\\[-\\Ocxcm*u", "fill": "ascii"}]},
        {"spans": [{"text": "            ^1jt1)+_}{?--:.  .]__I_):                        l]<-+[[i!!I/|[}1(JC/|r_<t||)-1UaLfuOW,", "fill": "ascii"}]},
        {"spans": [{"text": "       .l-j|[1+({[\\j|_.      ,|]<]|i                          ._-?|t}_-~[_~:`.      ^j-1]<I{ux//xct:", "fill": "ascii"}]},
        {"spans": [{"text": " .'-{nJYu1[[+\")[txj,         \\1;![i                              ..                 .t?+!_)})[]|\\|f\"", "fill": "ascii"}]},
        {"spans": [{"text": "']QLCuUvx[[____??)\"        ._\\___l                                                   ^)[-?{}{]?{/r^\"", "fill": "ascii"}]},
        {"spans": [{"text": "   .l\\uUrx(|1\\[11_         :{{{{i                                                     .~\\}~[(}ff\"  \"", "fill": "ascii"}]},
        {"spans": [{"text": "                          ;f)]1>                                                          ...      ", "fill": "ascii"}]},
        {"spans": [{"text": " ", "fill": "text"}]},
        
        # --- BIO SECTION ---
        {"spans": [{"text": "soham@machine", "fill": "name", "weight": "bold"}]},
        {"spans": [{"text": "-------------", "fill": "comment"}]},
        {"spans": [{"text": "Hi, I'm ", "fill": "text"}, {"text": "Soham Kharabe", "fill": "name", "weight": "bold"}]},
        {"spans": [{"text": "I am an ", "fill": "text"}, {"text": "AIML B.Tech student", "fill": "accent"}, {"text": " specializing in Artificial Intelligence.", "fill": "text"}]},
        {"spans": [{"text": "Focused on building ", "fill": "text"}, {"text": "innovative AI solutions", "fill": "label"}, {"text": " and creative design.", "fill": "text"}]},
        {"spans": [{"text": " ", "fill": "text"}]},
        {"spans": [{"text": "Driven by a passion for neural networks and system architecture.", "fill": "text"}]}
    ]
}

def escape_xml(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def render_svg(config):
    c, l, clr = config["canvas"], config["layout"], config["colors"]
    svg_lines = []
    for i, line in enumerate(config["lines"]):
        y = l["top_y"] + (i * c["line_height"])
        tspans = []
        if "spans" in line:
            for s in line["spans"]:
                color = clr.get(s["fill"], s["fill"])
                weight = ' font-weight="bold"' if s.get("weight") == "bold" else ""
                tspans.append(f'<tspan fill="{color}"{weight}>{escape_xml(s["text"])}</tspan>')
        svg_lines.append(f'<text x="{l["left_x"]}" y="{y}" xml:space="preserve">{"".join(tspans)}</text>')
    
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{c["width"]}" height="{c["height"]}" viewBox="0 0 {c["width"]} {c["height"]}" font-family="{c["font_family"]}" font-size="{c["font_size"]}px">
    <rect width="100%" height="100%" fill="{clr["background"]}" rx="{c["radius"]}"/>
    {"".join(svg_lines)}
</svg>'''

if __name__ == "__main__":
    svg_content = render_svg(CONFIG)
    Path(CONFIG["output"]).write_text(svg_content, encoding="utf-8")
    print(f"Success! Saved to {CONFIG['output']}")