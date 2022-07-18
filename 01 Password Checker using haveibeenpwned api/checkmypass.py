import requests
import hashlib
import sys

def req_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RunTimeError(f'Error fetching: {res.status_code}, pls check the api and try again')
	return res

def get_password_leaks_count(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0

def pwned_api_checker(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first_5char, tail = sha1password[:5], sha1password[5:]
	response = req_api_data(first_5char)
	return get_password_leaks_count(response, tail)

def main(args):
	for password in args:
		count = pwned_api_checker(password)
		if count:
			print(f'{password} was found {count} times, you should probably change it...')
		else:
			print(f'{password} was NOT found; all good!')
	return 'done!'

if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))