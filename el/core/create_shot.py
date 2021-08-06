import os
from time import gmtime, strftime
from el.utils.read_dump import read_json, dump_json
from el.core.levels import Level
from el.utils.el import el


class CreateShot():

	@classmethod
	def check(cls):
		if Level.check():
			return True
		else:
			return False
	

	@classmethod
	def create_shot(cls, seq_num):
		shots_level_file = os.path.join(os.getcwd(), 'shots', 'shots.lvl')

		data = read_json(shots_level_file)
		SHOT_PREFIX = data['PREFIX'] + "_"

		BASE_SHOT_NUM = 200
		check = False

		# check if the seq exists
		sequences = data['all_seq']
		shots = data['all_shots']

		if seq_num in sequences:
			check = True
			if len(shots) == 0:
				shot_num =SHOT_PREFIX  + str(BASE_SHOT_NUM)
			
			else:
				last_shot_num = int(shots[-1][3:])
				shot_num =  SHOT_PREFIX + str(int(last_shot_num )+ 1)




		# ADD TO ALL_SHOTS
		data['all_shots'].append(shot_num)

		index = 0
		if check:
			seq_data = data['shots']['sequences']

			for seq in seq_data:
				if seq['sequence'].startswith(seq_num):
					break
				
				else:
					index = index + 1

			data['shots']['sequences'][index]['shots'].append(shot_num)

		seq_name = data['shots']['sequences'][index]['sequence']
		shot_num = shot_num

		# CREATE DIRECTORIES
		shot_path = os.path.join(os.getcwd(), 'shots', seq_name, shot_num)
		os.mkdir(shot_path)

		dump_json(shots_level_file, data)
		# SHOTS SUB DIRECTORIES

		# SHOTS JSON DATA
		created_on = strftime("%d %b %Y", gmtime())

		SHOT_DATA = {
			"sequence": seq_name,
			"shot_num": shot_num,
			"created-on": created_on
		}

		shot_lvl_file = os.path.join(shot_path, seq_name[:3]+'_' + shot_num + '.lv')

		dump_json(shot_lvl_file, SHOT_DATA)

		# ADD DATA TO SEQ LEVEL FILE
		seq_lvl_file = os.path.join(os.getcwd(), 'shots', seq_name, 'seq.lvl')
		data = {
			"shot_num": shot_num,
			"created-on": created_on
		}


		seq_lvl_data = read_json(seq_lvl_file)
		seq_lvl_data['shots'].append(data)
		# print(seq_lvl_data)
		dump_json(seq_lvl_file, seq_lvl_data)

		# create shot sub directory
		sub_dir_list = ['animation', 'fx', 'cfx', 'cache', 'maya', 'houdini', 'render', 'comp', 'lighting']
		for sub_dir in sub_dir_list:
			path = os.path.join(shot_path, sub_dir)  
			os.mkdir(path)





class CreateSeq():

	@classmethod
	def check(cls):
		if Level.check():
			return True
		else:
			return False

	
	@classmethod
	def create_seq(cls, seq_name):

		# READ SHOTS DATA
		shots_level_file = os.path.join(os.getcwd(), 'shots', 'shots.lvl')

		data = read_json(shots_level_file)
		BASE_SEQ = 400
		if len(data['all_seq']) == 0:
			if seq_name:
				seq_num = str(BASE_SEQ) + '_' + seq_name
			else:
				seq_num = str(BASE_SEQ)

			seq_num_only = seq_num[:3]

			data['all_seq'].append(str(seq_num_only))

		else:
			last_seq_number = data['all_seq'][-1][:3]
			seq_num = int(last_seq_number) + 1

			if seq_name:
				seq_num = str(seq_num) + "_" + seq_name

			# Strip the name
			seq_num = str(seq_num)
			seq_num_only = seq_num[:3]

			data['all_seq'].append(str(seq_num_only))

		seq_path = os.path.join(os.getcwd(), 'shots', str(seq_num))

		# Create directories
		os.mkdir(seq_path)

		created_on = strftime("%d %b %Y", gmtime())

		# create shot json file
		seq_data = {
				"sequence":seq_num,
				"created-on": created_on,
				"shots":[]
				}

		data['shots']['sequences'].append(seq_data)

		seq_level_file = os.path.join(seq_path, 'seq.lvl')
		dump_json(seq_level_file, seq_data)


		dump_json(shots_level_file, data=data)


		## MESSAGE
		el.echo("New Sequence Created")
		el.echo(f"{seq_num}")