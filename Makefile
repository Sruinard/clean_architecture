

all:
	echo "Starting Deployment"
	./setup/infra.sh
clean:
	rm -rf ./backend/.azure
.PHONY: all clean
	
