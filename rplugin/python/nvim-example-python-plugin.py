import neovim


@neovim.plugin
class NeotagsPlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.autocmd('BufWritePost', pattern='*', eval='expand("<afile>:p")')
    def update_tags_for_file(self, filename):
        self.nvim.out_write('neotags > ' + message + "\n")
