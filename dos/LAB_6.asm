bits 16
org 0x100

global _start

section .data
input_message_ax: db "Insert AX =",24h,
input_message_dx: db 10,"Insert DX =",24h,
output_message_ax: db 10, "AX = ",24h 
output_message_dx: db 10, "DX = ",24h

section .text

_start:
	xor ax,ax
	xor dx,dx
	mov ah,09
	lea dx, input_message_ax
	int 21h
	call .input_hex
	shl di,4
	mov bx,di
	call .input_hex
	add bx, di
	mov ah,09
	lea dx, input_message_dx
	int 21h
	call .input_hex
	shl di,4
	mov dx,di
	call .input_hex
	add dx, di
	mov ax, bx
	call .print_bin
	ret
.print_bl:
	push ax
	push bx
	xor bx,bx
	mov bl,al
	mov ah,2
	push bx
	pop bx
	pop ax
	ret
.input_hex:
	push ax
	push dx
.start_hex:
	xor ax,ax
	xor dx,dx
	mov ah,8
	int 21h
	mov dl,al
	cmp al,30h
	jb .error_value
	cmp al,39h
	ja .al_grant_39
	clc
	xor ah,ah
	mov di,ax
	sub di,30h
.print_char:
	jc .start_hex
	mov dl,al
	mov ah,2
	int 21h
	pop dx
	pop ax
	ret

.error_value:
	stc
	jmp .start_hex
	
.al_grant_39:
	cmp al,41h
	jb .error_value
	cmp al,46h
	ja .error_value
	xor ah,ah
	mov di,ax
	sub di,37h
	clc
	jmp .print_char
 

.print_bin:
	push ax
	push dx
	mov si, ax
	mov di, dx
	xor ax,ax
	xor dx,dx
	mov ah,09
	lea dx, output_message_ax
	int 21h
	mov ah,02
	mov cx, 10h
.print_bin_si:
	mov dl, 00h
	rcl si,1
	adc dl,30h
	int 21h
	loop .print_bin_si
	mov ah,09
	mov dx, output_message_dx
	int 21h
	mov ah,02
	mov cx, 10h
.print_bin_di:
	clc
	mov dl, 00h
	rcl di,1
	adc dl,30h
	int 21h
	loop .print_bin_di
	pop dx
	pop ax
	ret


