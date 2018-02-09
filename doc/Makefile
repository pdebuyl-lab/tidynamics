# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = tidynamics
SOURCEDIR     = .
BUILDDIR      = _build

SSH_HOST=
SSH_PORT=22
SSH_USER=
SSH_TARGET_DIR=/home/pierre/lab_html/tidynamics

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

rsync_upload: html
	rsync -e "ssh -p $(SSH_PORT)" -P -rvz --delete $(BUILDDIR)/html/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)/ --cvs-exclude

.PHONY: help Makefile rsync_upload

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
