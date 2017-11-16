

count = 0
for i in xrange(50):
    print "doing loop "+str(i)
    file = open("/Volumes/HDD/TFG/DeepFashion/Category and Attribute Prediction Benchmark/Anno/list_category_img.txt")
    writefile = open("prueba-"+str(i)+".txt", "w")
    line = file.readline()
    while True:
        split = line.split()
        if count > 1:
            if int(split[1]) is i:
                writefile.write(line)
        count = count + 1
        line = file.readline()
        if not line: break
    file.close()
    writefile.close()
    count = 0

print "Finished"