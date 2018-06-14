let SessionLoad = 1
if &cp | set nocp | endif
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd /project2/rossby/group07/pyqg_mod
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +0 ../build.sh
badd +0 kernel.pyx
badd +0 model.py
badd +6 ../pyqg_pip/__init__.py
badd +0 qg_model.py
badd +1926 ~/.vimrc
badd +530 ~/.bashrc
badd +23 /project2/rossby/group07/pyqg_pip/model.py
badd +2 ../pyqg_pip/qg_model.py
args ../build.sh
edit ../build.sh
set splitbelow splitright
wincmd t
set winheight=1 winwidth=1
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=10
setlocal fen
silent! normal! zE
let s:l = 6 - ((5 * winheight(0) + 21) / 43)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
6
normal! 04|
tabedit kernel.pyx
set splitbelow splitright
wincmd t
set winheight=1 winwidth=1
argglobal
setlocal fdm=manual
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=10
setlocal fen
silent! normal! zE
29,29fold
30,30fold
34,34fold
35,35fold
39,39fold
40,40fold
42,42fold
44,44fold
45,45fold
46,46fold
47,47fold
49,49fold
50,50fold
51,51fold
52,52fold
54,54fold
55,55fold
56,56fold
59,59fold
60,60fold
61,61fold
62,62fold
66,66fold
67,67fold
70,70fold
71,71fold
72,72fold
73,73fold
77,77fold
80,80fold
81,81fold
82,82fold
86,86fold
90,90fold
91,91fold
92,92fold
93,93fold
96,96fold
98,98fold
101,101fold
102,102fold
103,103fold
104,104fold
105,105fold
106,106fold
107,107fold
108,108fold
110,203fold
207,208fold
209,210fold
211,212fold
213,214fold
215,216fold
217,218fold
219,220fold
221,222fold
224,233fold
235,244fold
249,249fold
246,254fold
259,259fold
256,264fold
267,268fold
276,276fold
270,310fold
312,313fold
324,324fold
315,350fold
352,353fold
357,357fold
358,358fold
355,368fold
370,372fold
377,377fold
378,378fold
379,379fold
380,380fold
381,381fold
374,433fold
436,437fold
438,441fold
444,445fold
446,453fold
455,456fold
457,463fold
465,466fold
469,469fold
468,470fold
472,473fold
474,475fold
477,478fold
479,482fold
484,485fold
487,487fold
486,489fold
491,492fold
494,494fold
493,498fold
500,501fold
503,504fold
506,507fold
509,510fold
512,513fold
515,516fold
518,520fold
522,523fold
525,526fold
528,529fold
531,532fold
534,535fold
32,535fold
540,543fold
549,549fold
550,550fold
545,551fold
558,558fold
559,559fold
560,560fold
553,561fold
32
normal! zo
355
normal! zo
let s:l = 128 - ((21 * winheight(0) + 21) / 43)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
128
normal! 014|
tabedit model.py
set splitbelow splitright
wincmd t
set winheight=1 winwidth=1
argglobal
setlocal fdm=manual
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=10
setlocal fen
silent! normal! zE
86,204fold
207,225fold
227,230fold
233,252fold
254,264fold
266,342fold
346,368fold
370,374fold
378,414fold
416,418fold
420,422fold
424,426fold
428,435fold
437,438fold
440,441fold
444,466fold
471,486fold
492,502fold
505,508fold
540,542fold
554,556fold
558,570fold
572,600fold
602,604fold
606,608fold
610,612fold
614,629fold
631,641fold
643,655fold
657,659fold
661,667fold
670,673fold
676,679fold
21,679fold
21
normal! zo
let s:l = 479 - ((23 * winheight(0) + 21) / 43)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
479
normal! 010|
tabedit qg_model.py
set splitbelow splitright
wincmd t
set winheight=1 winwidth=1
argglobal
setlocal fdm=manual
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=99
setlocal fml=1
setlocal fdn=10
setlocal fen
silent! normal! zE
61,109fold
115,142fold
144,159fold
161,168fold
170,191fold
193,207fold
210,213fold
217,220fold
224,230fold
232,240fold
242,320fold
18,320fold
18
normal! zo
let s:l = 106 - ((21 * winheight(0) + 21) / 43)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
106
normal! 014|
tabnext 3
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
let g:this_session = v:this_session
let g:this_obsession = v:this_session
let g:this_obsession_status = 2
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
