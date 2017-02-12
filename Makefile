all: flite_hts_tamil

flite_hts_tamil: my_flite_hts_imp.c us_int_accent_cart.c us_int_tone_cart.c us_nums_cart.c us_phrasing_cart.c us_pos_cart.c transliterator.c
	gcc -lm -o $@ $^

clean:
	rm -fr *.o *.wav flite_hts_tamil

.PHONY: clean
