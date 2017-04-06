	.file	"1.c"
	.globl	s
	.section	.rodata
.LC0:
	.string	"hello"
	.data
	.align 8
	.type	s, @object
	.size	s, 8
s:
	.quad	.LC0
	.text
	.globl	main
	.type	main, @function
main:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$112, %rsp
	leaq	-112(%rbp), %rax
	movl	$99, %edx
	movq	%rax, %rsi
	movl	$0, %edi
	movl	$0, %eax
	call	read
	movl	%eax, -4(%rbp)
	movl	-4(%rbp), %eax
	subl	$1, %eax
	cltq
	movb	$0, -112(%rbp,%rax)
	leaq	-112(%rbp), %rax
	movl	$0, %esi
	movq	%rax, %rdi
	movl	$0, %eax
	call	open
	movl	%eax, -8(%rbp)
	leaq	-112(%rbp), %rcx
	movl	-8(%rbp), %eax
	movl	$100, %edx
	movq	%rcx, %rsi
	movl	%eax, %edi
	movl	$0, %eax
	call	read
	movl	%eax, -4(%rbp)
	movq	s(%rip), %rax
	movl	$5, %edx
	movq	%rax, %rsi
	movl	$1, %edi
	movl	$0, %eax
	call	write
	movl	$0, %eax
	leave
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu 5.2.1-22ubuntu2) 5.2.1 20151010"
	.section	.note.GNU-stack,"",@progbits
