# Tool tải truyện tranh VTLoader
# Site suport
# Beeng, TruyenVN, TruyenQQ, Truyentranh24, TCTruyen

#get link from command. Not require
from sys import argv
from tqdm import tqdm

# each module has its own website
import truyenqq
import beeng
import truyentranh24
import truyenvn
import tctruyen
import nettruyen

TRUYENQQ = 'http://truyenqq.com'
BEENG = 'https://beeng.net'
TRUYENTRANH24 = 'https://truyentranh24.com'
TRUYENVN = 'https://truyenvn.com'
TCTRUYEN = 'https://tctruyen.com'
NETTRUYEN = 'http://www.nettruyen.com'

# scriptname and link
lenArgv = 2

def handleLink(link):
	if link.startswith(BEENG):
		try:
			all_chap = beeng.get_chap(link)
			print('\n-> Detected\n-> Website:', beeng.hostname, '\n-> Manga: ', beeng.get_truyen(link),'\n-> Chapter: ', len(all_chap),'\n\n')
			askDown = input('Download Manga (y/n): ')
			if askDown.lower().strip() in ('y', 'yes'):
				print('\nStart Download...\n')
				with tqdm(total = len(all_chap), desc = 'All Chapter',unit = "MB",ncols = 80,position=0) as lbar:
					for d in reversed(all_chap):
						chap_url = d.attrs['href']
						all_img = beeng.get_img(chap_url)
						with tqdm(total = len(all_img), desc = beeng.get_name_chap(chap_url),unit = "MB",ncols = 80,leave=False,position=1) as pbar:
							for x in range(len(all_img)):
								beeng.dl_img(all_img[x],beeng.get_truyen(link),beeng.get_name_chap(chap_url),chap_url,x)
								pbar.update(1)
						lbar.update(1)
		except:
			exit()
	elif link.startswith(TRUYENQQ):
		try:
			all_chap = truyenqq.get_chap(link)
			print('\n-> Detected\n-> Website:', truyenqq.hostname, '\n-> Manga: ', truyenqq.get_truyen(link),'\n-> Chapter: ', len(all_chap),'\n\n')
			askDown = input('Download Manga (y/n): ')
			if askDown.lower().strip() in ('y', 'yes'):
				print('\nStart Download...\n')
				with tqdm(total = len(all_chap), desc = 'All Chapter',unit = "MB",ncols = 80,position=0) as lbar:
					for d in reversed(all_chap):
						chap_url = d.attrs['href']
						all_img = truyenqq.get_img(chap_url)
						with tqdm(total = len(all_img), desc = truyenqq.get_name_chap(chap_url),unit = "MB",ncols = 80,leave=False,position=1) as pbar:
							for x in range(len(all_img)):
								truyenqq.dl_img(all_img[x],truyenqq.get_truyen(link),truyenqq.get_name_chap(chap_url),chap_url,x)
								pbar.update(1)
						lbar.update(1)
		except:
			exit()
	elif link.startswith(TRUYENTRANH24):
		try:
			all_chap = truyentranh24.get_chap(truyentranh24.get_id(link))
			print('\n-> Detected\n-> Website :', truyentranh24.hostname, '\n-> Manga : ', truyentranh24.get_truyen(link),'\n-> Chapter : ', len(all_chap),'\n\n')
			askDown = input('Download Manga (y/n): ')
			if askDown.lower().strip() in ('y', 'yes'):
				print('\nStart Download...\n')
				with tqdm(total = len(all_chap), desc = 'All Chapter',unit = "MB",ncols = 80,position=0) as lbar:
					for d in all_chap:
						chap_url = link + '/' + d
						all_img = truyentranh24.get_img(chap_url)
						with tqdm(total = len(all_img), desc = truyenqq.get_name_chap(chap_url),unit = "MB",ncols = 80,leave=False,position=1) as pbar:
							for x in range(len(all_img)):
								truyentranh24.dl_img(all_img[x],truyentranh24.get_truyen(link),truyentranh24.get_name_chap(chap_url),chap_url,x)
								pbar.update(1)
						lbar.update(1)
		except:
			exit()
	elif link.startswith(TRUYENVN):
		try:
			all_chap = truyenvn.get_chap(link)
			print('\n-> Detected\n-> Website :', truyenvn.hostname, '\n-> Manga : ', truyenvn.get_truyen(link),'\n-> Chapter : ', len(all_chap),'\n\n')
			askDown = input('Download Manga (y/n): ')
			if askDown.lower().strip() in ('y', 'yes'):
				print('\nStart Download...\n')
				with tqdm(total = len(all_chap), desc = 'All Chapter',unit = "MB",ncols = 80,position=0) as lbar:
					for d in reversed(all_chap):
						chap_url = d.attrs['href']
						all_img = truyenvn.get_img(truyenvn.get_id(chap_url))
						with tqdm(total = len(all_img), desc = truyenvn.get_name_chap(chap_url),unit = "MB",ncols = 80,leave=False,position=1) as pbar:
							for x in range(len(all_img)):
								truyenvn.dl_img(all_img[x],truyenvn.get_truyen(link),truyenvn.get_name_chap(chap_url),chap_url,x)
								pbar.update(1)
						lbar.update(1)
		except:
			exit()
	elif link.startswith(TCTRUYEN):
		try:
			all_chap = tctruyen.get_chap(link)
			print('\n-> Detected\n-> Website :', tctruyen.hostname, '\n-> Manga : ', tctruyen.get_truyen(link),'\n-> Chapter : ', len(all_chap),'\n\n')
			askDown = input('Download Manga (y/n): ')
			if askDown.lower().strip() in ('y', 'yes'):
				print('\nStart Download...\n')
				with tqdm(total = len(all_chap), desc = 'All Chapter',unit = "MB",ncols = 80,position=0) as lbar:
					for d in reversed(all_chap):
						chap_url = d.attrs['href']
						chuong = chap_url.split("/")[-1].split(".")[0]
						all_img = tctruyen.get_img(chap_url)
						with tqdm(total = len(all_img), desc = chuong,unit = "MB",ncols = 80,leave=False,position=1) as pbar:
							for x in range(len(all_img)):
								link_img = all_img[x]
								if (link_img.find('data-comic') == 28):
									ai = x
								else:
									ai = x + 1
								tctruyen.dl_img(link_img,tctruyen.get_truyen(link),chuong,chap_url,ai)
								pbar.update(1)
						lbar.update(1)
		except:			
			exit()
	elif link.startswith(NETTRUYEN):
		try:
			all_chap = nettruyen.get_chap(link)
			print('\n-> Detected\n-> Website :', nettruyen.hostname, '\n-> Manga : ', nettruyen.get_truyen(link),'\n-> Chapter : ', len(all_chap),'\n\n')
			askDown = input('Download Manga (y/n): ')
			if askDown.lower().strip() in ('y', 'yes'):
				print('\nStart Download...\n')
				with tqdm(total = len(all_chap), desc = 'All Chapter',unit = "MB",ncols = 80,position=0) as lbar:
					for d in reversed(all_chap):
						chap_url = d.attrs['href']
						chuong = nettruyen.get_name_chap(chap_url).split('-')[1]
						all_img = nettruyen.get_img(chap_url)
						with tqdm(total = len(all_img), desc = chuong,unit = "MB",ncols = 80,leave=False,position=1) as pbar:
							for x in all_img:
								nettruyen.dl_img(x,nettruyen.get_truyen(link),chuong,chap_url)
								pbar.update(1)
						lbar.update(1)
		except:			
			exit()
def main():
	# if get link from argv
	if lenArgv == len(argv):
		link = argv[1]
	# else require from input
	else:
		link = input('Input Link: ')
	# go to check the link
	handleLink(link)

if __name__ == '__main__':
	print('Bạn đang sử dụng tool tải truyện VTLoader\nTool hỗ trợ các site:\nBeeng,TruyenVN,Truyentranh24,Truyenqq,TCTruyen,Nettruyen.\nĐể tải truyện nhập link truyện tại bên dưới\n\n')
	main()