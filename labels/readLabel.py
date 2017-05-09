def get_label(x):
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
