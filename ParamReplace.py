import os
import re
import sys
import argparse
import urllib.parse
from colorama import *
from requests.utils import requote_uri


class param_replace():

	def __init__(self):

		init(autoreset=True)

		self.total_url = []
		self.param_name = "=" + str(args.param)


		if args.method == "1" or args.method == "2" or args.method == "3":
			pass

		else:
			print(Fore.MAGENTA+"Wrong Method. You can only Use 1 2 3 For The --method Parameter")

			sys.exit()


		if args.list and not args.stdin:

			if not os.path.exists(args.list):

				print(Fore.MAGENTA+"URL LIST NOT FOUND: {args.list}")

				sys.exit()

			with open(args.list, "r", encoding="utf-8") as f:

				[self.param_change(x) for x in f.read().split("\n") if x and "=" in str(x)]


		elif args.stdin and not args.list:

			[self.param_change(x) for x in sys.stdin.read().split("\n") if x and "=" in str(x)]

		else:

			print(Fore.MAGENTA+"WRONG PARAMS..")

			sys.exit()


	def param_change(self,url):
		
		url = url.replace("=&","=1&")
		
		if url.endswith("="):
			url = str(url) + "1"

		param_list = []
		
		parse = list(urllib.parse.parse_qs(url).keys())
		
		if not parse:
			pass
		
		else:
		
			alone_param = parse[0] + self.param_name
		
			for x in parse:
				param_list.append(x + self.param_name)

			multi_param = ("&").join(param_list)
			self.edit(alone_param,multi_param,url)

	def edit(self,alone_param,multi_param,url):
		
		alone_param = requote_uri(alone_param)
		multi_param = requote_uri(multi_param)

		if args.method == "1":

			if not alone_param in self.total_url:

				self.total_url.append(alone_param)

				if args.output:

					self.print_now(alone_param)

				print(Fore.MAGENTA+str(alone_param))


		elif args.method == "2":

			if not multi_param in self.total_url:

				self.total_url.append(multi_param)

				if args.output:

					self.print_now(multi_param)

				print(Fore.MAGENTA+str(multi_param))

		else:

			if "&" in url:

				if not alone_param in self.total_url:

					self.total_url.append(alone_param)

					if args.output:

						self.print_now(alone_param)

					print(Fore.MAGENTA+str(alone_param))


				if not multi_param in self.total_url:

					self.total_url.append(multi_param)

					if args.output:

						self.print_now(multi_param)

					print(Fore.MAGENTA+str(multi_param))

			else:

				if not alone_param in self.total_url:

					self.total_url.append(alone_param)

					if args.output:

						self.print_now(alone_param)

					print(Fore.MAGENTA+str(alone_param))


	def print_now(self,target_url):

		with open(args.output, "a+", encoding="utf-8") as file:

			file.write(str(target_url) + "\n")



if __name__ == "__main__":

	ap = argparse.ArgumentParser()

	ap.add_argument("-l", "--list", metavar="", required=False, help="READ URLS FROM LIST")
	ap.add_argument("-s", "--stdin", action="store_true", required=False, help="READ URLS FROM STDIN")
	ap.add_argument("-m", "--method", default="3", type=str, metavar="", required=False, help="PARAMETER PARSING METHOD(DEFAULT-3)")
	ap.add_argument("-p", "--param", default="FUZZ", type=str, metavar="", required=False, help="PARAM NAME(DEFAULT-FUZZ)")
	ap.add_argument("-o", "--output", metavar="", required=False, help="Save Output")

	args = ap.parse_args()

	start_replace = param_replace()
