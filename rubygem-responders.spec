#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-responders
Version  : 2.2.0
Release  : 8
URL      : https://rubygems.org/downloads/responders-2.2.0.gem
Source0  : https://rubygems.org/downloads/responders-2.2.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
# Responders
[![Gem Version](https://fury-badge.herokuapp.com/rb/responders.svg)](http://badge.fury.io/rb/responders)
[![Build Status](https://api.travis-ci.org/plataformatec/responders.svg?branch=master)](http://travis-ci.org/plataformatec/responders)
[![Code Climate](https://codeclimate.com/github/plataformatec/responders.svg)](https://codeclimate.com/github/plataformatec/responders)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n responders-2.2.0
gem spec %{SOURCE0} -l --ruby > rubygem-responders.gemspec

%build
gem build rubygem-responders.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
responders-2.2.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/responders-2.2.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/MIT-LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/action_controller/respond_with.rb
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/action_controller/responder.rb
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/generators/rails/USAGE
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/generators/rails/responders_controller_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/generators/rails/templates/api_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/generators/rails/templates/controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/generators/responders/install_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/responders.rb
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/responders/collection_responder.rb
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/responders/controller_method.rb
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/responders/flash_responder.rb
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/responders/http_cache_responder.rb
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/responders/locales/en.yml
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/responders/location_responder.rb
/usr/lib64/ruby/gems/2.3.0/gems/responders-2.2.0/lib/responders/version.rb
/usr/lib64/ruby/gems/2.3.0/specifications/responders-2.2.0.gemspec
