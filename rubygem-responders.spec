#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-responders
Version  : 2.1.0
Release  : 3
URL      : https://rubygems.org/downloads/responders-2.1.0.gem
Source0  : https://rubygems.org/downloads/responders-2.1.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
# Responders
[![Gem Version](https://fury-badge.herokuapp.com/rb/responders.png)](http://badge.fury.io/rb/responders)
[![Build Status](https://api.travis-ci.org/plataformatec/responders.png?branch=master)](http://travis-ci.org/plataformatec/responders)
[![Code Climate](https://codeclimate.com/github/plataformatec/responders.png)](https://codeclimate.com/github/plataformatec/responders)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n responders-2.1.0
gem spec %{SOURCE0} -l --ruby > rubygem-responders.gemspec

%build
gem build rubygem-responders.gemspec

%install
gem_dir=$(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .${gem_dir} \
--bindir .%{_bindir} \
responders-2.1.0.gem

mkdir -p %{buildroot}${gem_dir}
cp -pa .${gem_dir}/* \
%{buildroot}${gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/responders-2.1.0.gem
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/RespondWith/ClassMethods/cdesc-ClassMethods.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/RespondWith/ClassMethods/clear_respond_to-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/RespondWith/ClassMethods/respond_to-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/RespondWith/cdesc-RespondWith.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/RespondWith/respond_with-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/api_behavior-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/api_location-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/call-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/cdesc-Responder.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/controller-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/default_action-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/default_render-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/display-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/display_errors-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/format-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/has_errors%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/has_renderer%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/json_resource_errors-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/navigation_behavior-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/navigation_location-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/request-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/resource-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/resource_errors-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/resource_location-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/resources-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/respond-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/response_overridden%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/to_format-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/to_html-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/Responder/to_js-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/ActionController/cdesc-ActionController.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Rails/Generators/RespondersControllerGenerator/attributes_params-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Rails/Generators/RespondersControllerGenerator/cdesc-RespondersControllerGenerator.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Rails/Generators/RespondersControllerGenerator/flash%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Rails/Generators/cdesc-Generators.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Rails/cdesc-Rails.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/CollectionResponder/cdesc-CollectionResponder.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/CollectionResponder/navigation_location-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/ControllerMethod/cdesc-ControllerMethod.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/ControllerMethod/responders-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/FlashResponder/cdesc-FlashResponder.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/FlashResponder/flash_keys-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/FlashResponder/helper-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/FlashResponder/namespace_lookup-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/FlashResponder/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/FlashResponder/set_flash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/FlashResponder/set_flash_message%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/FlashResponder/set_flash_now%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/FlashResponder/to_html-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/FlashResponder/to_js-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/Generators/InstallGenerator/cdesc-InstallGenerator.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/Generators/InstallGenerator/copy_locale-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/Generators/InstallGenerator/create_responder_file-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/Generators/InstallGenerator/update_application-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/Generators/InstallGenerator/update_application_controller-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/Generators/cdesc-Generators.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/HttpCacheResponder/cdesc-HttpCacheResponder.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/HttpCacheResponder/do_http_cache%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/HttpCacheResponder/do_http_cache%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/HttpCacheResponder/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/HttpCacheResponder/persisted%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/HttpCacheResponder/to_format-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/LocationResponder/cdesc-LocationResponder.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/LocationResponder/included-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/Railtie/ActiveSupport/cdesc-ActiveSupport.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/Railtie/cdesc-Railtie.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/Responders/cdesc-Responders.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/responders-2.1.0/ri/lib/generators/rails/page-USAGE.ri
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/MIT-LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/README.md
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/action_controller/respond_with.rb
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/action_controller/responder.rb
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/generators/rails/USAGE
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/generators/rails/responders_controller_generator.rb
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/generators/rails/templates/controller.rb
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/generators/responders/install_generator.rb
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/responders.rb
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/responders/collection_responder.rb
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/responders/controller_method.rb
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/responders/flash_responder.rb
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/responders/http_cache_responder.rb
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/responders/locales/en.yml
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/responders/location_responder.rb
/usr/lib64/ruby/gems/2.2.0/gems/responders-2.1.0/lib/responders/version.rb
/usr/lib64/ruby/gems/2.2.0/specifications/responders-2.1.0.gemspec
