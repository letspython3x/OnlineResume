from flask import Flask, request

app = Flask(__name__)

automated_responses = {
    'Name': 'AB Abhi',
    'Email Address': 'letspython3.x@gmail.com',
    'Phone': '8575368593444',
    'Position': 'Python Developer',
    'Years': '4',
    'Referrer': 'XYZ company',
    'Degree': "Bachelor's degree - Computer Science",
    'Status': 'Yes',
    'Resume': 'url/for/resume',
    'Source': 'url/for/resume',
    'Ping': 'OK',
}


@app.route('/', methods=['GET'])
def index():
    query = request.args.get('q', None)
    description = request.args.get('d', None)
    print("Ping: %s --- %s" % (query, description))
    if query in automated_responses:
        return automated_responses[query]
    elif query == 'Puzzle':
        return "Will solve"
        # return solve_puzzle(description)
    else:
        return "Can't say"


def parse_to_matrix(puzzle):
    puzzle_mat = []
    print(type(puzzle), puzzle)
    puzzle = str(puzzle.strip()).split("\n")
    print(puzzle)
    for pos, line in enumerate(puzzle):
        if pos == 0 or pos == 1:
            continue
        else:
            puzzle_mat.append(list(line[1:]))
    return puzzle_mat


def parse_to_str(puzzle_mat):
    newline = '\n'
    temp = ' ABCD' + newline
    for pos, row in enumerate(puzzle_mat):
        t = temp[pos + 1] + ''.join([r for r in row]) + newline
        temp += t
    return temp


def solve_puzzle(puzzle):
    puzzle_mat = parse_to_matrix(puzzle)
    puzzle_mat = level_1(puzzle_mat)
    puzzle_mat_2 = level_2(puzzle_mat)
    puzzle_mat_2 = level_2(puzzle_mat_2)
    puzzle = parse_to_str(puzzle_mat_2)
    return puzzle


def level_1(mat_1):
    mat_2 = [['-' for i in range(len(mat_1))] for j in range(len(mat_1[0]))]
    for pos_i, i in enumerate(mat_1):
        for pos_j, j in enumerate(mat_1[pos_i]):
            if pos_i == pos_j:
                mat_2[pos_i][pos_j] = '='
            else:
                if mat_1[pos_i][pos_j] == '>':
                    mat_2[pos_i][pos_j] = '>'
                    mat_2[pos_j][pos_i] = '<'
                elif mat_1[pos_i][pos_j] == '<':
                    mat_2[pos_i][pos_j] = '<'
                    mat_2[pos_j][pos_i] = '>'
    return mat_2


def level_2(mat_1):
    mat_2 = [[mat_1[i][j] for i in range(len(mat_1))] for j in range(len(mat_1[0]))]
    for pos_i, i in enumerate(mat_1):
        for pos_j, j in enumerate(mat_1[pos_i]):
            if not (pos_i == pos_j) and mat_1[pos_i][pos_j] == '-':
                for k in range(4):
                    if pos_j != k and pos_i != k:
                        # print(pos_i, k, pos_j, k)
                        if mat_1[pos_i][k] == mat_1[k][pos_j] and mat_1[k][pos_j] != '-':
                            # print('---', pos_i, k, pos_j, k)
                            mat_2[pos_i][pos_j] = '>' if mat_1[k][pos_j] == '<' else '<'
    return mat_2


if __name__ == "__main__":
    app.run(port=8000, debug=True)

# ssh -i ~/Downloads/mike_aws_key_pair.pem ubuntu@ec2-13-59-211-216.us-east-2.compute.amazonaws.com
# sudo python3 flask_balihoo/resume_balihoo_rest_service.py
# vim flask_balihoo/resume_balihoo_rest_service.py
# puzzle = r"ABCD\nA=-->\nB--<-\nC---<\nD-->-"
#     # puzzle = r"ABCD\nA=->-\nB-=<-\nC<---\nD>---"
#     # puzzle = r"ABCD\nA=->-\nB-=-<\nC--->\nD--<-"
#     # puzzle = r"ABCD\nA--<-\nB-=->\nC--=<\nD-->-"
#     # puzzle = r"ABCD\nA-<--\nB>=--\nC->--\nD<--="

