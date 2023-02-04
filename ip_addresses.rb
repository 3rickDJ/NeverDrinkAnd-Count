addresses = 2**32

d,c,b,a = 1,0,0,0
def update(a,b,c,d)
  a += 1
  a = 0; b += 1 if a == 255
  b = 0; c += 1 if b == 255
  c = 0; d += 1 if c == 255
  d = 0         if d == 255
  [d,c,b,a]
end

file = File.open('burstmodejeje.md', 'a+')
addresses.times do
  a += 1
  if a == 255
    a = 0
    b +=1
  end
  if b == 255
    b = 0
    c +=1
  end
  if c == 255
    c = 0
    d +=1
  end
  if d == 255
    d = 0
    c = 0
    b = 0
    a = 0
  end
  file << "1. #{d}.#{c}.#{b}.#{a}\n"
end
file.close
