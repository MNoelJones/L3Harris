all: l3harris

l3harris: l3harris.o
	g++ -o l3harris $<

%.o: %.c
	g++ -o $@ $<