org 10
in_port:
    .word 0
out_port:
    .word 1
line_feed:
    .word 10

_start:
    in in_port
    out out_port
    jmp _start
    halt