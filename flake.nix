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

        hugo-coder = pkgs.runCommandLocal "hugo-coder" {
          src = theme;
        }
        ''
          cp -r $src $out
          chmod -R u+w $out
        '';
      in {
        devShell = pkgs.mkShell {
          name = "blog-shell";

          buildInputs = [ pkgs.hugo ];

          shellHook = ''
            mkdir -p themes
            ln -snf "${hugo-coder}" themes/hugo-coder
          '';
        };
      }
    );
}
