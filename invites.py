def invites(s):
    invites = s.split(';')
    invites = sorted(invites)

    byLastName = []
    for invite in invites:
        invite = invite.split(':')
        if len(invite) != 2:
            raise ValueError('Separator is missing')

        byLastName.append('(' + invite[1].upper() + ', ' + invite[0].upper() + ')')

    byLastName = sorted(byLastName)
    return ''.join(byLastName)

name_of_invites = "Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"
print(invites(name_of_invites))