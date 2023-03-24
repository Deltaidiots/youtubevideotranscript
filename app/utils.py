def process_transcript(lines):
    transcript = ''
    for line in lines:
        text = ' '.join(line.split()[1:]).strip()
        transcript += ' ' + text
    return ' '.join(transcript.split())
