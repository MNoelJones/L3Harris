IFNAME=enp0s3

venv: .venv
	pipenv install

run: venv
	pipenv run python l3harris.py --files --procs --mac --ifname ${IFNAME}