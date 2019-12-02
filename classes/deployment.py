"""."""
import os
import shutil

LARAVEL = """
    location / {
        try_files $uri /index.php?$query_string;
    }
    location ~ \.php$ {
        try_files $uri /index.php?$query_string;
        fastcgi_index index.php;

        # Create a no cache flag
        set $no_cache "";

        # Don't ever cache POSTs
        if ($request_method = POST) {
            set $no_cache 1;
        }
        # General FastCGI handling
        fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;
        fastcgi_pass_header Set-Cookie;
        fastcgi_pass_header Cookie;
        fastcgi_ignore_headers Cache-Control Expires Set-Cookie;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_param SCRIPT_FILENAME $request_filename;
        fastcgi_intercept_errors on;
        include fastcgi_params;
    }
"""

VUE = """
    location / {
        try_files $uri $uri/ /index.html;
    }
"""

WORDPRESS = """
    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        try_files $uri /index.php?$query_string;
        fastcgi_index index.php;

        # Create a no cache flag
        set $no_cache "";

        # Don't ever cache POSTs
        if ($request_method = POST) {
            set $no_cache 1;
        }
        # Admin stuff should not be cached
        if ($request_uri ~* "/(wp-admin/|wp-login.php)") {
            set $no_cache 1;
        }

        # If we are the admin, make sure nothing
        # gets cached, so no weird stuff will happen
        if ($http_cookie ~* "wordpress_logged_in_") {
            set $no_cache 1;
        }

        # Cache and cache bypass handling
        fastcgi_no_cache $no_cache;
        fastcgi_cache_bypass $no_cache;
        fastcgi_cache microcache;
        fastcgi_cache_key $scheme$request_method$server_name$request_uri$args;
        fastcgi_cache_valid 200 60m;
        fastcgi_cache_valid 404 10m;
        fastcgi_cache_use_stale updating;



        # General FastCGI handling
        fastcgi_pass unix:/var/run/php/php7.2-fpm.sock;
        fastcgi_pass_header Set-Cookie;
        fastcgi_pass_header Cookie;
        fastcgi_ignore_headers Cache-Control Expires Set-Cookie;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_param SCRIPT_FILENAME $request_filename;
        fastcgi_intercept_errors on;
        include fastcgi_params;
    }
"""

PATH = os.getcwd()


class Deployment:
    """."""

    def __init__(self, target, domain):
        """."""
        self.target = target
        self.domain = domain
        self.project = domain.split('.')[0]

        if not os.path.exists('deployment'):
            os.makedirs('deployment')

    def create(self):
        """."""
        try:
            print('Creating domain folder \n')
            shutil.copytree('src/domain', 'deployment/{}'.format(self.domain))
        except Exception:
            print('Folder already exists \n')
            pass
        try:
            print('Creating git hook folder \n')
            shutil.copytree('src/domain.git', 'deployment/{}.git'.format(self.project))
        except Exception:
            print('Folder already exists \n')
            pass

        try:
            print('Creating nginx file\n')
            shutil.copyfile('src/domain.conf', 'deployment/{}.conf'.format(self.project))
        except Exception:
            print('Folder already exists \n')
            pass

    def setup(self):
        """."""
        with open('deployment/{}.conf'.format(self.project)) as f:
            N = f.read().replace('DOMAIN', self.domain).replace('PATH', PATH)
            if self.target == 'laravel':
                N = N.replace('TARGET', LARAVEL)
            elif self.target == 'vue':
                N = N.replace('TARGET', VUE)
            elif self.target == 'wordpress':
                N = N.replace('TARGET', WORDPRESS)
        with open('deployment/{}.conf'.format(self.project), 'w') as f:
            f.write(N)

        with open('deployment/{}.git/hooks/post-receive'.format(self.project)) as f:
            G = f.read().replace('PATH', PATH).replace('DOMAIN', self.domain)
        with open('deployment/{}.git/hooks/post-receive'.format(self.project), 'w') as f:
            f.write(G)

    def clear(self):
        """."""
        shutil.rmtree('deployment')
