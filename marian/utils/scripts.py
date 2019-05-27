def join_bash_scripts(scripts):
    """
    have the option of creating a wrapper script for every group of bash files
    to be run, or just join them on the fly.
    """

    if len(scripts) < 2:
        raise NotImplementedError

    output_script = scripts[0]

    for script in scripts[1:]:
        output_script = output_script + ''.join(script.splitlines(True)[1:])

    return output_script

def open_files(filenames):
    """open files and return contents."""

    return list(map(lambda file: open(file, 'r').read(), filenames))
