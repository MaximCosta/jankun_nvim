import neovim


@neovim.plugin
class NeotagsPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim


    def echo(self, *msgs):
        msg = ' '.join([str(m) for m in msgs])
        self.nvim.out_write(msg + '\n')

    def echo_error(self, *msgs):
        msg = ' '.join([str(m) for m in msgs])
        self.nvim.err_write(msg + '\n')

    @neovim.autocmd('BufWritePost', pattern='*', eval='expand("<afile>:p")')
    def update_tags_for_file(self, filename):
        self.nvim.out_write('neotags > ' + message + "\n")

    @neovim.autocmd('BufWritePost', pattern='*')
    def echo_test(self):
        self.echo("je suis lambda")

    @neovim.function('DoItPython')
    def doItPython(self, args):
        self.vim.command('echo "hello from DoItPython"')
