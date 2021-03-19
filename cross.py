import math

def create_cross(length):
  center_index = math.floor(length / 2)
  cross = ''
  for i in range(length):
      if ( i == center_index ):
          for x in range(length):
              cross += '*'
      else:
          for x in range(length):
              if (x == center_index):
                  cross += '*'
              else:
                  cross += '-'
      if (i < (length - 1)):
        cross += '\n'

  return cross

print(create_cross(7))