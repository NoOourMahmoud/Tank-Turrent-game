import cx_Freeze

executables = [cx_Freeze.Executable("TankTutorial.py")]

cx_Freeze.setup(
	name = "TankTurrent" ,
	options = {"build_exe":{"packages":["pygame"],
	"include_files":["Ball_Bounce-Popup_Pixels-172648817.wav",
	"Fire Crackers-SoundBible.com-1716803209.wav",
	"Kids Cheering-SoundBible.com-681813822.wav",
	"ray_gun-Mike_Koenig-1169060422.wav",
	"Sad_Trombone-Joe_Lamb-665429450.wav",
	"Ta Da-SoundBible.com-1884170640.wav"]}},
	discription = "TankTurrent Game Tutorial" ,
	executables = executables
	)
