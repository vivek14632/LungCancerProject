import os


def get_label(x):
	mUser=os.getlogin()
	# root is the user at the CIRCE
	if(mUser=='vivek4'):
		#its a circe cluster
		fp=open('/work/v/vivek4/stage1_total_labels.csv')
	elif(mUser=='vivek'):
		fp=open('/home/vivek/stage1_total_labels.csv')
	elif(mUser=='root'):
		fp=open('/work/v/vivek4/stage1_total_labels.csv')
	else:
		fp=open('/home/ravi/stage1_labels.csv')
	m_data=fp.readlines()[1:]
	fp.close()
	for m_row in m_data:
		m_row=m_row.split('\n')[0]
		m_row=m_row.split(',')
		if(m_row[0]==x):
			return m_row[1]

def main():
	label=get_label('0015ceb851d7251b8f399e39779d1e7d')
	print(label)
if __name__ == '__main__':
	main()
