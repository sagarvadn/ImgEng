from PIL import Image, ImageDraw, ImageFont
filepath = 'quotes.txt'
#replace fontname with your fontname
#change font size i.e. 70, if needed
fnt = ImageFont.truetype('fonts/fontname.ttf', 70)

with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		#print("Line {}: {}".format(cnt, line.strip()))
		img = Image.open("quotes-back.png")
		d = ImageDraw.Draw(img)
		img_w, img_h =img.size
		x1 = img_w
		y1 = img_h - (round( img_h / 10 ))

		sentence = line.strip()
		quote = sentence.upper()
		sum = 0
		for letter in quote:
			sum += d.textsize(letter, font=fnt)[0]
		average_length_of_letter = sum/len(quote)
		#find the number of letters to be put on each line
		number_of_letters_for_each_line = (x1/1.618)/average_length_of_letter
		incrementer = 0
		fresh_quote = ''
		#add some line breaks
		for letter in quote:
		  if(letter == '='):
		    fresh_quote += '\n' + '-'
		  elif(incrementer < number_of_letters_for_each_line):
		    fresh_quote += letter
		  else:
		    if(letter == ' '):
		      fresh_quote += '\n'
		      incrementer = 0
		    else:
		      fresh_quote += letter
		  incrementer+=1
		#render the text in the center of the box
		dim = d.textsize(fresh_quote, font=fnt)
		x2 = dim[0]
		y2 = dim[1]
		qx = (x1/2 - x2/2)
		qy = (y1/2-y2/2)
		d.text((qx,qy), fresh_quote ,align="center",  font=fnt, fill=(0,0,0))
		img_name = 'output/quote_' + str(cnt) + '.png'
		img.save(img_name)
		print("Line {}: {}".format(cnt, fresh_quote))
		line = fp.readline()
		cnt += 1
