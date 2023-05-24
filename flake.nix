{
  description = "JesusMtnez's blog";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    theme = {
      url = "github:luizdepra/hugo-coder";
      flake = false;
    };
  };

  outputs = { self, nixpkgs, flake-utils, theme }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        themeName = ((builtins.fromTOML (builtins.readFile "${theme}/theme.toml")).name);
      in
      {

        packages.blog = pkgs.stdenv.mkDerivation rec {
          name = "blog";
          versino = "0.0.1";
          src = ./.;
          nativeBuildInputs = [ pkgs.hugo ];
          configurePhase = ''
            mkdir -p "themes/${themeName}"
            cp -r ${theme}/* "themes/${themeName}"
          '';
          buildPhase = "hugo";
          installPhase = "cp -r public $out";
        };

        defaultPackage = self.packages.${system}.blog;

        devShell = pkgs.mkShell {
          name = "blog-shell";
          packages = [ pkgs.hugo ];
          shellHook = ''
            mkdir -p "themes/${themeName}"
            cp -r ${theme}/* "themes/${themeName}"
          '';
        };
      }
    );
}
