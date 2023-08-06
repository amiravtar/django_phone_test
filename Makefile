clear_log:
	./scripts/clear_log.sh
clear_cash:
	find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
