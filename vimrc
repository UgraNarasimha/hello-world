set number
set tabstop=2
set t_Co=256
syntax on
colorscheme monokai
set runtimepath+=~/.vim/bundle/nerdtree
autocmd vimenter * NERDTree
nmap <F6> :NERDTreeToggle<CR>