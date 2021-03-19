def convert_to_wall(number):
    return f'{number:064b}'

def convert_to_number(wall):
    # convert a sequence of 1s and 0s into a 64-bit number
    return int(wall, 2)

def generate_fixed_wall(number_representation, repair_kits, attacked_places):
    binary = convert_to_wall(number_representation)
    print(binary, ' binary orig')
    # revbin = binary[::-1]
    #
    # for idx in attacked_places:
    #     revbin = revbin[:idx] + '0' + revbin[idx + 1:]
    #     # print(revbin, idx)

    for idx in attacked_places:
        binary = binary[:idx] + '0' + binary[idx + 1:]

    revbin = binary[::-1]
    print(revbin[::-1], ' binary attacked')


    for idx in range(len(revbin) - 1):
        #print('idx', idx)
        if repair_kits <= 0:
            break
        else:
            if revbin[idx] == '0' and revbin[idx + 1] == '0' and repair_kits > 0:
                for idx2 in range(idx, len(revbin)):
                    if revbin[idx2] == '0' and repair_kits > 0:
                        # print(idx2)
                        revbin = revbin[:idx2] + '1' + revbin[idx2 + 1:]
                        idx += 1
                        repair_kits -= 1
                    else:
                        # print('pasok')
                        # print(idx2)
                        idx += 1
                        break

    binary = revbin[::-1]
    print(binary, ' binary fixed')

    return convert_to_number(binary)
    pass

binary = generate_fixed_wall(1234567890, 4, [55, 36])
print(convert_to_wall(1100353246), ' binary expected fixed')
print(binary)

binary = generate_fixed_wall(23555678, 2, [43, 54, 61])
print(convert_to_wall(23555546), ' binary expected fixed')
print(binary)