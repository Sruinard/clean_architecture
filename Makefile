

all:
	@ echo "Hello World"
	@ mkdir just_a_test
clean:
	@ rm -rf just_a_test
.PHONY: all clean
