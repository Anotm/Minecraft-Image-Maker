from Cimpl import *
import math



def pixel_info_extractor(file_name: str) -> list:
  """
  
  Inpute: Text file name containing available blocks and their average 
  colour that will be used as pixels.
  (Must contain full file names and no unnecessary spaces
  with each line being a new image)
  Example: "pixels.txt"
  
  Outpute: List containing tuples of block information.
  (Name, Red, Green, Blue)
  """
  
  file = open(file_name, "r")
  block_info = []
  
  for line in file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    name, r, g, b = line_list[0], line_list[1], line_list[2], line_list[3],
    block_info.append( (name, float(r), float(g), float(b)) )
  
  file.close()
  return(block_info)

def mc_image_converter(image: Image, blocks: list) -> list:
  """
  
  Inpute: Image file to be converted to mincraft and list containing
  blocks that will be used as pixels
  
  Outpute: List containing lists of tuples with block name and their
  x, y location.
  
  """
  
  main_list = []
  
  for y in range(0, get_height(image)):
    line_list = []
    for x in range(0, get_width(image)):
      i_r, i_g, i_b = get_color(image, x, y)
      closest = 195075
      block_index = 0
      block_name = 'a'
      for i in range(len(blocks)):
        name, b_r, b_g, b_b = blocks[i]
        color_diff_r = (i_r - b_r)*(i_r - b_r)
        color_diff_g = (i_g - b_g)*(i_g - b_g)
        color_diff_b = (i_b - b_b)*(i_b - b_b)
        diff = math.sqrt(color_diff_r + color_diff_g + color_diff_b)
        if diff < closest:
          closest = diff
          block_index = i
          block_name = name
      line_list.append((block_name, x, y))
    main_list.append(line_list)
    
    
  return main_list

def list_2_mc(pic_info) -> list:
    #/setblock <pos> <block> [destroy¦keep¦replace]
    #/setblock ~1 ~1 ~1 minecraft:white_wool replace
    main_list = []
    for i in pic_info:
        for j in i:
            name, x, z = j
            x += 1
            z += 1
            command = 'setblock ~' + str(x) + ' ~1 ~' + str(z) + ' minecraft:' + name + ' replace'
            #command2 = 'give @p minecraft:' + name
            #if command2 not in main_list:
            main_list.append(command)
    return (main_list)

def main():
  main_image = load_image(choose_file())
  block_pixle_list = pixel_info_extractor("pixels.txt")
  image_list = mc_image_converter(main_image, block_pixle_list)
  mc_image = list_2_mc(image_list)

  with open('angel.txt', 'w') as file:
      file.writelines("%s\n" % command for command in mc_image)
  print("done")

if if __name__ == '__main__':
  main()











'''
# MAKE THE LIST TO MINECRAFT-CODE FUNTION

L = pixel_info_extractor("pixels.txt")
m = mc_image_converter(main_image, L)
print(m[0][0], m[100][100], m[130][130])

blocks = pixel_info_extractor("pixels.txt")
print(blocks)
print()

i_r, i_g, i_b = get_color(main_image, 17, 130)
print(i_r, i_g, i_b)
print()
closest = 195075
block_index = 0
block_name = 'a'
for i in range(len(blocks)):
  name, b_r, b_g, b_b = blocks[i]
  color_diff_r = (i_r - b_r)*(i_r - b_r)
  color_diff_g = (i_g - b_g)*(i_g - b_g)
  color_diff_b = (i_b - b_b)*(i_b - b_b)
  diff = math.sqrt(color_diff_r + color_diff_g + color_diff_b)
  print (diff)
  if diff < closest:
    closest = diff
    block_index = i
    block_name = name
    print()
    print (block_index, block_name)
    print()

print (block_index, block_name)
'''