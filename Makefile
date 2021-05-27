

all:
	@ echo "Hello World"
	@ mkdir just_a_test
	./setup/test.sh
clean:
	@ rm -rf just_a_test
	rm -rf ./backend/.azure
.PHONY: all clean
	
