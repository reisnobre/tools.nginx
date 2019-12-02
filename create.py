"""."""
#!/usr/local/bin/python3
# os.rename('domain', DOMAIN)
# os.rename('domain.conf', DOMAIN + '.conf')
#
# shutil.copytree('domain', DOMAIN)
# shutil.copytree('./repos/domain.git', './repos/' + DOMAIN + '.git')
#
# with open('domain.conf') as f:
#     N = f.read().replace('DOMAIN', DOMAIN).replace('PATH', PATH)
#     if TYPE == '--php':
#         N = N.replace('TYPE', PHP)
#     elif TYPE == '--html':
#         N = N.replace('TYPE', HTML)
#     elif TYPE == '--cms':
#         N = N.replace('TYPE', CMS)
#
#
# with open(DOMAIN + '.conf', 'w') as f:
#     f.write(N)
#
# with open('post-receive') as f:
#     G = f.read().replace('PATH', PATH).replace('DOMAIN', DOMAIN)
#
# with open('./repos/' + DOMAIN + '.git/hooks/post-receive', 'w') as f:
#     f.write(G)
