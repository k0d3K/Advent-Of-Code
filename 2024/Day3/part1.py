# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part1.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/01 11:29:36 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/03 07:42:47 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re

with open("input", 'r') as file:
    data = file.read().replace('\n', '')

mul = 0
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, data)
mul += sum(int(x) * int(y) for x, y in matches)

print("The sum of valid multiplications is:", mul)