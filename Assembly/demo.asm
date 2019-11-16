
                ;a demo program for ng linh about the assembly 



global  _start 
section .text
                ;must declare for linker
_start:
    mov edx, len ;message length 
    mov ecx, msg ;message to write 
    mov ebx, 1; 
    mov eax, 4 ; system call number (sys_write)
    int 0x80 ; call kernel

section .data

msg     db 'Hello World!', 0xa
len     equ $ - msg 