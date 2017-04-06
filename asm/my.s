	.file	"1.c"
	.section	.text.unlikely,"ax",@progbits
.LCOLDB0:
	.section	.text.startup,"ax",@progbits
.LHOTB0:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
	subq	$120, %rsp
	movl	$99, %edx
	xorl	%edi, %edi
	movq	%rsp, %rsi
	xorl	%eax, %eax
    syscall
	subl	$1, %eax
	movq	%rsp, %rdi
	xorl	%esi, %esi
	cltq
	movb	$0, (%rsp,%rax)
	xorl	%eax, %eax
    mov $0x02, %al
    syscall
	movq	%rsp, %rsi
	movl	%eax, %edi
	movl	$100, %edx
	xorl	%eax, %eax
    syscall
	movq	%rsp, %rsi
	movl	%eax, %edx
	movl	$1, %edi
	xorl	%eax, %eax

    mov $0x01, %al
    syscall
	xorl	%eax, %eax
	addq	$120, %rsp
	ret
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE0:
	.section	.text.startup
.LHOTE0:
	.ident	"GCC: (Ubuntu 5.2.1-22ubuntu2) 5.2.1 20151010"
	.section	.note.GNU-stack,"",@progbits
