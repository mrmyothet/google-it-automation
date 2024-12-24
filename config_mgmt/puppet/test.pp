describe 'gsku', :type => class do
  let (:facts){ { 'is_virtual' => 'false' }}
  it { should contain_package('gsku').with_ensure('latest')}
end
